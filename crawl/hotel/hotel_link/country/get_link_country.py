import time
import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


with open('./country.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    driver_path = "./chromedriver"
    driver_service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    options.page_load_strategy = 'none'
    options.add_argument('disable-popup-blocking')
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.implicitly_wait(10)
    # time.sleep(5)
    list_links = []
    for row in reader:
        country_name = row[0]
        # Replace the country name in the link
        modified_link = "https://www.tripadvisor.com/Search?q=" + country_name.lower()

        driver.get(modified_link)
        try:
            # Get the link to the hotels in each country
            content = driver.find_element(By.CSS_SELECTOR, "div[class*='ui_columns is-mobile result-content-columns'").get_attribute('onclick')
            start_index = content.find("'/") + 2
            end_index = content.find("'", start_index)

            result = content[start_index:end_index].replace("Tourism", "Hotels").replace("Vacations", "Hotels")
            
            if result[-11:] == 'Hotels.html':
                print(result)
                list_links.append(result)
        except:
            pass
    # Quit the driver and close the browser
    driver.quit()
    #Write to csv file
    with open('./country/link_country.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for link in list_links:
            writer.writerow([link])