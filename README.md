# Property-Data-Scraper

This repository contains two Python scripts for collecting and searching property data. The first script is used for scraping property data from a specific website and saving it into a CSV file. The second script searches this CSV file for property details based on legal descriptions.

## Dependencies

Both scripts require specific Python packages to function correctly. Before running the scripts, ensure you have the following dependencies installed:

- beautifulsoup4
- selenium
- webdriver-manager
- requests
- pandas

You can install all required dependencies with the following command:

```bash
pip install -r requirements.txt
```

1. Property Data Scraper (main.py)
This script uses Selenium and BeautifulSoup to scrape property data from "https://polaris3g.mecklenburgcountync.gov/address/". It navigates to each property's page by incrementing an ID in the URL, extracts the legal description and address, and saves the data into property_data.csv.

Usage
To run the script, execute:

```bash
python main.py
```
The script will create a file named property_data.csv and populate it with property data fetched from the web. You can adjust the range of pages to scrape by modifying the range in the for-loop.

2. Property Data Search (search_engine.py)
This script loads the data collected by the scraper from property_data.csv and allows the user to search for properties by entering a legal description. It supports case-insensitive substring matching.

Usage
To start the search interface, run:

```bash
python search_engine
```
Enter a legal description to search for. Type 'exit' to quit the program.

Notes
Ensure that the chromedriver executable is compatible with your installed version of Chrome and is properly set up in your PATH or specified in the script.
Modify the range in the scraper script according to the number of pages you intend to scrape.
