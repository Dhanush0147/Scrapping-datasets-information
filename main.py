from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests
import time
import json

# Configure Selenium WebDriver to use Firefox in headless mode
firefox_options = Options()
firefox_options.add_argument("--headless")  
firefox_options.add_argument("--disable-gpu")  
firefox_options.add_argument("--no-sandbox")  

# Initialize the Firefox WebDriver with the specified options
service = Service()  # Automatically uses GeckoDriver in PATH
driver = webdriver.Firefox(service=service, options=firefox_options)

# Base URL for the dataset repository
base_url = "https://archive.ics.uci.edu"

def scrape_page(page_url):
    """
    Scrape data from a single page of the dataset repository.

    Parameters:
        page_url (str): The URL of the page to scrape.

    Returns:
        list: A list of dictionaries containing dataset information.
    """
    try:
        # Send a GET request to fetch the page HTML
        response = requests.get(page_url)
        if response.status_code != 200:
            print(f"Failed to fetch data from {page_url}. Status code: {response.status_code}")
            return []

        # Parse the page HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        data_list = []

        # Locate all dataset entries on the page
        topics = soup.find_all("a", class_="link-hover link text-xl font-semibold")
        
        # Process each dataset entry
        for topic in topics:
            title = topic.text.strip()
            dataset_url = base_url + topic["href"]  # Construct the full dataset URL

            # Use Selenium to load the dataset page and retrieve dynamic content
            driver.get(dataset_url)
            time.sleep(2)  # Wait for the page to load

            # Parse the dynamically loaded content using BeautifulSoup
            dataset_soup = BeautifulSoup(driver.page_source, "html.parser")

            # Extract details such as subject area, description, views, and feature count
            subject_area = extract_element_text(dataset_soup, 
                "body > div > div.drawer.h-full > div.drawer-content > main > div > div.col-span-12.flex.flex-col.gap-4.md\\:col-span-9 > div.flex.flex-col > div.relative.flex.flex-col.gap-4.bg-base-100.p-4.shadow > div.grid.grid-cols-8.gap-4.md\\:grid-cols-12 > div:nth-child(2) > p", 
                default="Unknown"
            )
            description = extract_element_text(dataset_soup, 
                "body > div > div.drawer.h-full > div.drawer-content > main > div > div.col-span-12.flex.flex-col.gap-4.md\\:col-span-9 > div.flex.flex-col > div.relative.flex.flex-col.gap-4.bg-base-100.p-4.shadow > div:nth-child(1) > div > p > span", 
                default="No description available."
            )
            views = extract_element_text(dataset_soup, 
                "body > div > div.drawer.h-full > div.drawer-content > main > div > div.col-span-12.md\\:col-span-3 > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > span", 
                default="0"
            )
            features_count = extract_element_text(dataset_soup, 
                "body > div > div.drawer.h-full > div.drawer-content > main > div > div.col-span-12.flex.flex-col.gap-4.md\\:col-span-9 > div.flex.flex-col > div.relative.flex.flex-col.gap-4.bg-base-100.p-4.shadow > div.grid.grid-cols-8.gap-4.md\\:grid-cols-12 > div:nth-child(6) > p", 
                default="Unknown"
            )

           
            data_list.append({
                "title": title,
                "description": description,
                "subject_area": subject_area,
                "views": views,
                "features": features_count,
            })

        return data_list
    except Exception as e:
        print(f"Error occurred while scraping {page_url}: {e}")
        return []

def extract_element_text(soup, selector, default="N/A"):
    """
    Extract the text of an element using a CSS selector.

    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object.
        selector (str): The CSS selector of the target element.
        default (str): The default value if the element is not found.

    Returns:
        str: The extracted text or the default value.
    """
    element = soup.select_one(selector)
    return element.text.strip() if element else default
# List to store all scraped data
all_data = []

# Number of pages to scrape (can be adjusted)
num_pages = 4
for page in range(1, num_pages + 1):
    page_url = f"{base_url}/datasets?orderBy=DateDonated&sort=desc&page={page}"
    print(f"Scraping page {page}...")
    page_data = scrape_page(page_url)
    all_data.extend(page_data)

# Save the scraped data to a JSON file
output_file = "uci_datasets.json"
with open(output_file, "w") as json_file:
    json.dump(all_data, json_file, indent=4)

print(f"Scraped data from {num_pages} pages and saved to {output_file}.")

# Close the Selenium WebDriver
driver.quit()
