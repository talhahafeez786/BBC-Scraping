from utils.common import scrape_bbc_section, save_to_csv

def scrape_innovation():
    section_url = "https://www.bbc.com/innovation"
    data = scrape_bbc_section(section_url)
    if data:
        save_to_csv(data, "innovation")

if __name__ == "__main__":
    scrape_innovation()
