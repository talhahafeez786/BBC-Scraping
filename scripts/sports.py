from utils.common import scrape_bbc_section, save_to_csv

def scrape_sport():
    section_url = "https://www.bbc.com/sport"
    data = scrape_bbc_section(section_url)
    if data:
        save_to_csv(data, "sport")

if __name__ == "__main__":
    scrape_sport()
