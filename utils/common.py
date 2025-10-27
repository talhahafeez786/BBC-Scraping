import csv
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# Setup requests session with retries
def get_session():
    retry_strategy = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


# Clean text
def clean_text(text):
    if not text:
        return ""
    return " ".join(text.replace("\n", " ").replace("\r", " ").split())


# Fetch BBC Article Details
def get_article_details(url, session, headers):
    try:
        response = session.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("h1")
        title = clean_text(title_tag.get_text()) if title_tag else ""

        date_tag = soup.find("time")
        published_date = date_tag.get("datetime") if date_tag else ""

        author_tag = (
            soup.find("span", class_="sc-95d8ad4d-1") or
            soup.find("span", class_="byline__name")
        )
        author = clean_text(author_tag.get_text()) if author_tag else "BBC News"

        paragraphs = soup.select("article p")
        full_text = " ".join(clean_text(p.get_text()) for p in paragraphs)

        return {
            "title": title,
            "published_date": published_date,
            "author": author,
            "content": full_text
        }

    except requests.exceptions.Timeout:
        print(f"Timeout fetching article: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Request error scraping {url}: {e}")
    except Exception as e:
        print(f"Unexpected error scraping {url}: {e}")
    return None


# Scrape BBC Section (with restricted divs)
def scrape_bbc_section(section_url):
    session = get_session()
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/141.0.0.0 Safari/537.36"
        )
    }

    print(f"\n🔍 Fetching BBC section: {section_url}")
    response = session.get(section_url, headers=headers, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove restricted/unwanted divs
    for selector in [
        "div.sc-1907e52a-0.fZLsBL",
        "div.ssrcss-m5j4pi-MetadataContent.eh44mf00",
        "div[data-testid='iowa-section']",
        "div[data-testid='styled-container']",
        "div.ssrcss-1wsw50m-SimpleCollectionsWrapper.e1lr2am02",
        "div[data-testid='illinois-section-5']"
    ]:
        for tag in soup.select(selector):
            tag.decompose()

    main_section = soup.find(id="main-content")
    if not main_section:
        print("⚠️ Could not find #main-content section.")
        return []

    base_url = "https://www.bbc.com"
    results = []
    articles = main_section.select("a[href^='/'], a[href^='https://www.bbc.com/']")

    for i, a in enumerate(articles, start=1):
        link = a.get("href")
        if not link:
            continue
        if link.startswith("/"):
            link = base_url + link

        headline_tag = a.find(["h1", "h3", "strong"])
        headline = clean_text(headline_tag.get_text() if headline_tag else a.get_text())
        if not headline:
            continue

        parent = a.find_parent(["div", "article", "li", "p", "section"])
        img_tag = parent.find("img") if parent else None
        summary_tag = parent.find("p") if parent else None

        image = img_tag.get("src") if img_tag else ""
        summary = clean_text(summary_tag.get_text()) if summary_tag else ""

        if any(d["link"] == link for d in results):
            continue

        print(f"({i}) Scraping article: {headline[:60]}...")
        article_details = get_article_details(link, session, headers)

        time.sleep(random.uniform(1, 4))

        if article_details:
            results.append({
                "headline": headline,
                "link": link,
                "summary": summary,
                "image": image,
                **article_details
            })
        else:
            print(f"Skipped incomplete article: {link}")

    print(f"\n✅ Scraped {len(results)} complete articles from {section_url}.")
    return results


# Save to CSV
def save_to_csv(data, section_name):
    os.makedirs("output", exist_ok=True)
    filename = os.path.join("output", f"bbc_{section_name}.csv")

    keys = ["headline", "link", "summary", "image", "title", "published_date", "author", "content"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"💾 Saved {len(data)} records to {filename}")
