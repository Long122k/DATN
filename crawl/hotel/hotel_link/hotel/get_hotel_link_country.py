import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium webdriver
driver_path = "./chromedriver"
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(service=Service(driver_path), options=options)
driver.implicitly_wait(10)


links = []
data = []
domain = 'https://www.tripadvisor.com/'

with open('./country/link_country.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the first row
    for row in csv_reader:
        link = domain + row[0]
        links.append(link)
# url = "https://www.tripadvisor.com/Hotels-g293921-Vietnam-Hotels.html"
# url = 'https://www.tripadvisor.com/Hotels-g293921-oa300-Vietnam-Hotels.html'

for url in links:
# Open the URL in the Selenium webdriver
    country_name = url.split('-')[2]
    driver.get(url)

    page_source = driver.page_source
    # Create a BeautifulSoup object with the page source
    soup = BeautifulSoup(page_source, "html.parser")

    # Find the <a> tag with class "property_title prominent"
    a_tags = soup.find_all("a", class_="property_title prominent")

    # Extract the href attribute value
    for a_tag in a_tags:
        href = a_tag.get("href")
        data.append([country_name, href])
        print(href)
    
    time.sleep(20)

with open('./hotel/country_hotel_link.csv', 'w', newline='') as hotel_file:
    csv_writer = csv.writer(hotel_file)
    csv_writer.writerow(['Country', 'Link'])  # Write header
    csv_writer.writerows(data)
# Close the Selenium webdriver
driver.quit()
