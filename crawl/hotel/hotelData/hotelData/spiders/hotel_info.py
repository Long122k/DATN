import time
from datetime import datetime, timedelta
import scrapy
from scrapy import Selector
from selenium import webdriver
from scrapy.utils.project import get_project_settings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..items import HotelDataItem


class get_hotel(scrapy.Spider):
    name = 'hotel_info'
    allow_domain = ['tripadvisor.com']
    domain = 'https://www.tripadvisor.com/'
    links = ['https://www.tripadvisor.com/Hotel_Review-g60763-d23448880-Reviews-Motto_by_Hilton_New_York_City_Chelsea-New_York_City_New_York.html']
    start_urls = links

#     from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

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
        wait = WebDriverWait(driver, 30)

        driver.get(response.url)
        #time for loading expand button
        time.sleep(0.3)

        try:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ui_icon.caret-down.Lvqmo'))).click()
        except:
            pass

        hotel_name = driver.find_element(By.ID, 'HEADING').text if driver.find_elements(By.ID, 'HEADING') else 'NA'
        hotel_address = driver.find_element(By.CLASS_NAME, 'oAPmj').text if driver.find_elements(By.CLASS_NAME, 'oAPmj') else 'NA'
        price = driver.find_element(By.CLASS_NAME, 'gbXAQ').text if driver.find_elements(By.CLASS_NAME, 'gbXAQ') else 'NA'
        total_hotel_reviews = driver.find_element(By.CLASS_NAME, 'hkxYU').text.split(' ')[0] if driver.find_elements(By.CLASS_NAME, 'hkxYU') else 'NA'
        star = driver.find_element(By.CLASS_NAME, 'UctUV').get_attribute("aria-label").split(" of ")[0] if driver.find_elements(By.CLASS_NAME, 'UctUV') else 'NA'

        elements = driver.find_elements(By.CLASS_NAME, 'YibKl')
        for element in elements:
            review_date = element.find_element(By.XPATH, './/div[@class="cRVSd"]/span').text if element.find_elements(By.XPATH, './/div[@class="cRVSd"]/span') else 'NA'
            if review_date.split(' ')[-1] == "Yesterday":
                review_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
                reviewer_link = element.find_element(By.CLASS_NAME, 'ui_header_link').get_attribute('href') if element.find_elements(By.CLASS_NAME, 'ui_header_link') else 'NA'
                reviewer_rating = element.find_element(By.CLASS_NAME, 'ui_bubble_rating').get_attribute("class").split("_")[-1] if element.find_elements(By.CLASS_NAME, 'ui_bubble_rating') else 'NA'
                reviewer_contribution = element.find_element(By.CLASS_NAME, 'yRNgz').text if element.find_elements(By.CLASS_NAME, 'yRNgz') else 'NA'
                reviewer_title_comment = element.find_element(By.CLASS_NAME, 'Qwuub').text if element.find_elements(By.CLASS_NAME, 'Qwuub') else 'NA'
                reviewer_stay_date = element.find_element(By.CLASS_NAME, 'teHYY').text if element.find_elements(By.CLASS_NAME, 'teHYY') else 'NA'
                reviewer_trip_type = element.find_element(By.CLASS_NAME, 'TDKzw').text.split(' ')[-1] if element.find_elements(By.CLASS_NAME, 'TDKzw') else 'NA'
                reviewer_comment = element.find_element(By.CLASS_NAME, 'QewHA').text if element.find_elements(By.CLASS_NAME, 'QewHA') else 'NA'

                item = HotelDataItem()
                item['hotel_name'] = hotel_name
                item['total_hotel_reviews'] = total_hotel_reviews
                item['star'] = star
                item['hotel_address'] = hotel_address
                item['price'] = price
                item['review_date'] = review_date
                item['reviewer_rating'] = reviewer_rating
                item['reviewer_contribution'] = reviewer_contribution
                item['reviewer_link'] = reviewer_link
                item['reviewer_title_comment'] = reviewer_title_comment
                item['reviewer_comment'] = reviewer_comment
                item['reviewer_stay_date'] = reviewer_stay_date
                item['reviewer_trip_type'] = reviewer_trip_type

                yield item
            else:
                pass
        driver.quit()

