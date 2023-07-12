import time
import csv
from datetime import datetime, timedelta
from scrapy import Selector
import scrapy
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from ..items import SorturlItem

class GeturlSpider(scrapy.Spider):
    name = "getUrl"
    allowed_domains = ["tripadvisor.com"]
    # start_urls = ["https://www.tripadvisor.com/Hotel_Review-g293924-d2298266-Reviews-AIRA_Boutique_Hanoi_Hotel_Spa-Hanoi.html"]

    links = []

    def start_requests(self):
        start_index = 48000  # Index to start from
        counter = 0
        existing_urls = set()
        # with open('./test.csv', 'r') as existing_file:
        #     existing_reader = csv.reader(existing_file)
        #     next(existing_reader)
        #     for row in existing_reader:
        #         existing_urls.add(row[4])
        #     existing_file.close()

        with open('./unique_hotel.csv', 'r') as file:
            csv_reader = csv.reader(file)
            # next(csv_reader)
            for row in csv_reader:
                if counter < start_index:
                    counter += 1
                    continue
                if counter >= start_index + 10000:  # Break the loop after 100 iterations
                    break
                url = row[3]
                # if url not in existing_urls:
                city = row[0]
                country = row[1]
                hotel_id = row[2]
                yield scrapy.Request(url, self.parse, meta={'arg1': city, 'arg2': country, 'arg3': hotel_id})
                counter += 1


    def parse(self, response):
        setting = get_project_settings()
        driver_path = setting['CHROME_DRIVER']
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('disable-popup-blocking')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--blink-settings=imagesEnabled=false')

        driver = webdriver.Chrome(service=service, options=options)
        driver.get(response.url)

        hotel_url = response.url
        total_hotel_reviews = driver.find_element(By.CLASS_NAME, 'hkxYU').text.split(' ')[0] if driver.find_elements(By.CLASS_NAME, 'hkxYU') else 'NA'
        item = SorturlItem()
        item['url'] = hotel_url
        item['reviews'] = total_hotel_reviews
        item['city'] = response.meta['arg1']
        item['country'] = response.meta['arg2']
        item['hotel_id'] = response.meta['arg3']
        yield item

        driver.quit()
