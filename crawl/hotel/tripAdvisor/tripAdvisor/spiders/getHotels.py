import time
import scrapy
from selenium import webdriver  
from scrapy import Selector 
from ..items import HotelItem
from scrapy.utils.project import get_project_settings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class getHotels(scrapy.Spider):
    name = 'getHotels'
    allow_domain = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g293921-Vietnam-Hotels.html']

    def parse(self, response):
        setting = get_project_settings()
        driver_path = setting['CHROME_DRIVER']
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'none'
        options.add_argument('disable-popup-blocking')
        options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get(response.url)
        driver.implicitly_wait(30)

        # time.sleep(10)

    #browse the entire website
         # click more hotels
        # button = driver.find_element('xpath', '//button[@class="rmyCe _G B- z _S c Wc wSSLS pexOo sOtnj"]')
        # button.click()
        # button = driver.find_element(By.CSS_SELECTOR, 'button.rmyCe._G.B-.z._S.c.Wc.wSSLS.pexOo.sOtnj')
        # button.click()
        # time.sleep(3)
        # try:
        # h_url = driver.find_element("xpath",'//a[@class="BMQDV _F G- wSSLS SwZTJ FGwzt ukgoS"]')
        # for i in h_url:
        #     print(i.text)
        # parent = (driver.find_elements(By.CSS_SELECTOR,'div.ubodycon_main'))
        # h_url = driver.find_elements('xpath','//div[@class="listing_title "]/a')

        # h_url = driver.find_element('xpath','//div[@data-automation="hotel-card-title"]/a').get_attribute('href')
        h_url = driver.find_elements('xpath','//a[@class="property_title prominent "]')
        # h_url = driver.find_element('xpath','//a[@class="property_title prominent"]').get_attribute("href")
        # h_url = (response.xpath('//*[@id="lithium-root"]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/span/span/span/div/div/div[2]/header/div/div'))
        # except:
        # h_url = 'NA'
            # h_hotel_name = 'NA'
            # h_total_reviews = 'NA'
            # h_address = 'NA'
            # h_rating = 'NA'
        # h_url = response.xpath("/html/body/div/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/span/span/span/div/div/div[2]/header/div/div/a/@href")
        
#         href_list = [element.get_attribute('href') for element in h_url]
#         # for i in href_list:
#         #     print(i)
# # Print the href values
#         for href in href_list:
#             print(href)
        item = HotelItem()
        print(h_url)
        # print(len(h_url))
        # for i in h_url:
        #     # item['hotel_url'] = i.get_attribute('href')
        #     print(i.get_attribute('href'))
        # for i in range(0,len(h_url)):
        #     item['hotel_url'] = h_url[i].get_attribute('href')
        # item['hotel_name'] = h_hotel_name
        # item['total_reviews'] = h_total_reviews
        # item['address'] = h_address
        # item['rating'] = h_rating
        next_button = driver.find_element(By.XPATH, '//span[@class="nav next ui_button primary"]')
        time.sleep(20)

        print(next_button)
        # Check if the "Next" button is present
        if next_button:
            # Click the "Next" button
            next_button.click()

            # Wait for the new page to load
            WebDriverWait(driver, 10).until(EC.staleness_of(next_button))
            time.sleep(2)  # Optional: Add a small delay to ensure the page has fully loaded
        else:
            print("not load any more")
        yield item
        
        driver.quit()

        pass