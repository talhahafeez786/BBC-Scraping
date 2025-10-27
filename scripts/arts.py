from utils.common import scrape_bbc_section, save_to_csv

def scrape_arts():
    section_url = "https://www.bbc.com/arts"
    data = scrape_bbc_section(section_url)
    if data:
        save_to_csv(data, "arts")

if __name__ == "__main__":
    scrape_arts()
