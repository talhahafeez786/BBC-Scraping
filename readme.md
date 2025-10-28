# BBC Web Scraper

A Python-based web scraper that extracts news and articles from various sections of the BBC website.

## 📋 Project Structure

```
BBC-Scrapping/
├── output/               # Directory containing scraped data in CSV format
│   ├── bbc_home.csv
│   ├── bbc_arts.csv
│   ├── bbc_business.csv
│   ├── bbc_culture.csv
│   ├── bbc_earth.csv
│   ├── bbc_innovation.csv
│   ├── bbc_news.csv
│   ├── bbc_sport.csv
│   ├── bbc_travel.csv
├── scripts/              # Individual scraper modules
│   ├── home.py
│   ├── arts.py
│   ├── business.py
│   ├── culture.py
│   ├── earth.py
│   ├── innovation.py
│   ├── news.py
│   ├── sports.py
│   ├── travel.py
├── utils/                # Utility functions
├── main.py               # Main script to run the scraper
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/talhahafeez786/BBC-Scraping.git
   cd BBC-Scrapping
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠 Usage

1. **Run all scrapers**:
   ```bash
   python main.py
   ```

## 📊 Output

- All scraped data is saved in the `output/` directory as CSV files.
- Each file is named according to its section (e.g., `bbc_news.csv`).
- The CSV files contain article titles, URLs, and other relevant information.

## ⚠️ Note

- Please use this scraper responsibly and respect BBC's terms of service.
- Consider adding delays between requests to avoid overloading the server.
- The scraper might need updates if BBC changes its website structure.

## 📝 License

This project is for educational purposes only.
