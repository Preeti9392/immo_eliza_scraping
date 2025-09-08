# Immoweb Real Estate Scraper

This project provides a **web scraper for Belgian real estate listings** from [Immoweb](https://www.immoweb.be/). The scraper collects **property URLs** and extracts **detailed attributes** such as bedrooms, bathrooms, surface area, and building conditions. It leverages **multi-threading** for faster scraping and saves results into CSV files for further analysis or machine learning projects.

---

## 🚀 Project Overview

The scraper performs two main tasks:

1. **URL Collection**  
   - Generates base URLs for **houses and apartments** for a specified number of pages.  
   - Scrapes individual property URLs from search pages while ignoring new real estate projects.  
   - Saves the list of URLs to `immoweb_url_file.csv`.

2. **Property Attribute Extraction**  
   - Extracts property details (key-value pairs) from individual property pages.  
   - Scrapes information such as `bedroomCount`, `toilet_and_bath`, `habitableSurface`, `facedeCount`, `hasTerrace`, `totalParkingCount`, `type`, `subtype`, `province`, `locality`, `postCode`, `buildingCondition`, `epcScore`.  
   - Saves the extracted dataset to `dataset_file.csv`.  

---

## 🛠 Technologies & Libraries

- Python 3.9+
- Requests
- BeautifulSoup4
- Pandas
- Concurrent Futures (ThreadPoolExecutor)

---
📂 File Structure
```
├── scraper.py              # Main scraper class
├── immoweb_url_file.csv    # Scraped property URLs
├── dataset_file.csv        # Extracted property attributes
├── requirements.txt
├── gitignore
└── README.md


```

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/immoweb-scraper.git
cd immoweb-scraper

pip install -r requirements.txt

run main.py
