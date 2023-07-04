import scrapy
import csv
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from ..items import CityIntroItem


class GetIntroSpider(scrapy.Spider):
    name = "get_intro"
    allowed_domains = ["tripadvisor.com"]
    # start_urls = []
    # checkpoint_file = "checkpoint.json"  

    def __init__(self, *args, **kwargs):
        super(GetIntroSpider, self).__init__(*args, **kwargs)
        
    # def get_start_urls(self):
    #     with open('link_city_intro copy.csv', 'r') as file:
    #         reader = csv.DictReader(file)
    #         return [row['Link'] for row in reader]

    def start_requests(self):
    # Retrieve the last processed URL and meta data from the checkpoint file
        # last_processed_data = self.load_checkpoint()

        # If the checkpoint file exists, skip already processed URLs
        # if last_processed_data:
        #     last_processed_url = last_processed_data
        #     self.start_urls = self.start_urls[self.start_urls.index(last_processed_url) + 1:]

        with open('link_city_intro.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                url = row['Link']
                city_id = row['City_id']
                city_name = row['City_name']
                country_name = row['Country_name']

                # Check if the current URL matches the last processed URL
                # if last_processed_data and url == last_processed_url:
                #     # Continue from the last processed request
                #     yield scrapy.Request(url=url, callback=self.parse, meta=last_processed_data['meta'])
                # else:
                    # Start fresh for new requests
                yield scrapy.Request(url=url, callback=self.parse, meta={'city_id': city_id, 'city_name': city_name, 'country_name': country_name})


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

        wait = WebDriverWait(driver, 30)
        city_name = response.meta['city_name']
        country_name = response.meta['country_name']
        city_id = response.meta['city_id']
        try:
            city_image = driver.find_element(By.CSS_SELECTOR, '.neuYP img').get_attribute("src")
        except:
            city_image = 'NA'

        try:
            title = driver.find_element(By.CSS_SELECTOR, '.EDjsk .biGQs').text
        except:
            title = 'NA'

        try:
            intro = driver.find_element(By.CSS_SELECTOR, '.EDjsk .GYFPJ').text
        except:
            intro = 'NA'

        try:
            activity = []
            activity_elements = driver.find_elements(By.CSS_SELECTOR, '.NSbQk')
            for a in activity_elements:
                if a.find_element(By.CLASS_NAME, 'LNjrQ').text == 'Do':
                    activity = [x.text for x in a.find_elements(By.CLASS_NAME, 'keSJi')]
        except:
            activity = []

        driver.quit()

        item = CityIntroItem()
        item['city_id'] = city_id
        item['city_name'] = city_name
        item['country_name'] = country_name
        item['city_image'] = city_image
        item['title'] = title
        item['intro'] = intro
        item['activity'] = activity

        # self.save_to_cassandra(item)
        # self.update_checkpoint(response.url, {'meta': response.meta})
        yield item



    # def load_checkpoint(self):
    #     try:
    #         with open(self.checkpoint_file, 'r') as file:
    #             try:
    #                 data = json.load(file)
    #                 return data['url']
    #             except json.JSONDecodeError:
    #                 return None
    #     except FileNotFoundError:
    #         return None

    # def save_checkpoint(self, url):
    #     with open(self.checkpoint_file, 'a') as file:
    #         file.write(url)

    # def update_checkpoint(self, url, meta):
    #     data = {
    #         'url': url,
    #         'meta': meta
    #     }
    #     with open(self.checkpoint_file, 'w') as file:
    #         json.dump(data, file)

    # def closed(self, reason):
    #     self.session.shutdown()
    #     self.cluster.shutdown()