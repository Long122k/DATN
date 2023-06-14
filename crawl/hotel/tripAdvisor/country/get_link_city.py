import time
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import csv
from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


with open('crawl/city.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    driver_path = "/home/dolong/Documents/chromedriver_linux64/chromedriver"
    driver_service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    # options.page_load_strategy = 'none'
    options.add_argument('disable-popup-blocking')
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.implicitly_wait(10)
    # time.sleep(5)
    list_links = []
    for row in reader:
        city_name = row[1]
        country_name = row[4]
        # Replace the country name in the link
        modified_link = "https://www.tripadvisor.com/Search?q=" + quote(city_name.lower())

        driver.get(modified_link)
        try:
            # Get the link to the hotels in each country
            contents = driver.find_elements(By.CSS_SELECTOR, "div[class*='ui_columns is-mobile result-content-columns'")
            for content in contents:
                content = content.get_attribute('onclick')
                start_index = content.find("'/") + 2
                # print(content)
                if content[start_index:(start_index+7)] == 'Tourism':
                    end_index = content.find("'", start_index)

                    result = content[start_index:end_index].replace("Tourism", "Hotels").replace("Vacations", "Hotels")
                    
                    if result[-11:] == 'Hotels.html':
                        print(country_name)
                        city_id = result.split('-')[1]
                        list_links.append([city_id, city_name, country_name, result])
                    break
                else:
                   pass
                    
                    
        except:
            print("can't get data")
            pass
    # Quit the driver and close the browser
    driver.quit()
    #Write to csv file
    with open('crawl/hotel/tripAdvisor/country/link_city.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['City_id', 'City_name', 'Country_name', 'Link'])
        for link in list_links:
            writer.writerow(link)