from utils.common import scrape_bbc_section, save_to_csv

def scrape_business():
    section_url = "https://www.bbc.com/business"
    data = scrape_bbc_section(section_url)
    if data:
        save_to_csv(data, "business")

if __name__ == "__main__":
    scrape_business()
