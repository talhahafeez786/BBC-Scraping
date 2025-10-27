from utils.common import scrape_bbc_section, save_to_csv

def scrape_news():
    section_url = "https://www.bbc.com/news"
    data = scrape_bbc_section(section_url)
    if data:
        save_to_csv(data, "news")

if __name__ == "__main__":
    scrape_news()
