import time
import csv
import scrapy
from scrapy import Selector
from selenium import webdriver
from scrapy.utils.project import get_project_settings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..items import HotelItem


class get_hotel(scrapy.Spider):
    name = 'hotel'
    allow_domain = ['tripadvisor.com']
    domain = 'https://www.tripadvisor.com/'
    links = []

    def start_requests(self):
        with open('../country/link_city.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for _ in range(3376):  # Skip the rows until row 1669
                next(csv_reader)
            # next(csv_reader)  # Skip the first row
            for row in csv_reader:
                url = self.domain + row[3]
                city = row[1]
                country = row[2]
                yield scrapy.Request(url, self.parse, meta={'arg1': city, 'arg2': country})

    def parse(self, response):
        setting = get_project_settings()
        driver_path = setting['CHROME_DRIVER']
        options = webdriver.ChromeOptions()
        options.add_argument('disable-popup-blocking')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get(response.url)
        driver.implicitly_wait(30)

        url = []

        # Find all elements with class "property_title prominent"
        try:
            contents = driver.find_elements(By.XPATH, '//a[@class="property_title prominent "]')
            for element in contents:
                url.append(element.get_attribute('href'))
        except Exception as e:
            print("Error: ", e)

        for href in url:
            item = HotelItem()
            item['hotel_url'] = href
            item['hotel_id'] = href.split('-')[2]
            item['city'] = response.meta['arg1']
            item['country'] = response.meta['arg2']
            yield item

        driver.quit()
