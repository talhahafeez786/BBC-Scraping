from utils.common import scrape_bbc_section, save_to_csv

def scrape_travel():
    section_url = "https://www.bbc.com/travel"
    data = scrape_bbc_section(section_url)
    if data:
        save_to_csv(data, "travel")

if __name__ == "__main__":
    scrape_travel()
