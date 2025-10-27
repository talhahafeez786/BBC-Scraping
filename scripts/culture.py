from utils.common import scrape_bbc_section, save_to_csv

def scrape_culture():
    section_url = "https://www.bbc.com/culture"
    data = scrape_bbc_section(section_url)
    if data:
        save_to_csv(data, "culture")

if __name__ == "__main__":
    scrape_culture()
