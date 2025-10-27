from utils.common import scrape_bbc_section, save_to_csv

def scrape_earth():
    section_url = "https://www.bbc.com/future-planet"
    data = scrape_bbc_section(section_url)
    if data:
        save_to_csv(data, "earth")

if __name__ == "__main__":
    scrape_earth()
