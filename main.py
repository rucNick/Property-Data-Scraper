import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver for fetching legal description
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

filename = 'property_data.csv'

# Open a new CSV file to write data
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Legal Description', 'Legal Description Link', 'Address'])

    # Iterate through addresses
    for i in range(1, 100):  # Adjust the range as needed
        url = f"https://polaris3g.mecklenburgcountync.gov/address/{i}"  # Adjust ID accordingly
        driver.get(url)
        try:
            # Fetch legal description using Selenium, waiting 0.3 second
            legal_desc_element = WebDriverWait(driver, 0.3).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div/div[3]/main/div/div/div[2]/table/tbody/tr[1]/td[2]/a"))
            )
            legal_desc_link = legal_desc_element.get_attribute('href')
            legal_desc_text = legal_desc_element.text
        except TimeoutException:
            legal_desc_link = legal_desc_text = "N/A"

        # Fetch address using BeautifulSoup
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            address_element = soup.select_one("table.w-full.text-left.mb-2 thead.text-sm.font-normal + tbody tr td")
            address_text = address_element.get_text(strip=True) if address_element else "Not found"
        else:
            address_text = "Failed to retrieve address"

        # Only write to the CSV if the data is valid
        if not (legal_desc_text == "N/A" and address_text == "Failed to retrieve address"):
            writer.writerow([legal_desc_text, legal_desc_link, address_text])

# Close Selenium WebDriver
driver.quit()

print(f"Data saved to '{filename}'")
