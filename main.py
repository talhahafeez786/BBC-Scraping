from scripts import news, sports, business, innovation, culture, arts, travel, earth, home

def main():
    print("🚀 Starting BBC Multi-section Scraper...\n")
    home.scrape_home()
    # news.scrape_news()
    # sports.scrape_sport()
    # business.scrape_business()
    # innovation.scrape_innovation()
    # culture.scrape_culture()
    # arts.scrape_arts()
    # travel.scrape_travel()
    # earth.scrape_earth()

    print("\n✅ All sections scraped successfully!")

if __name__ == "__main__":
    main()
