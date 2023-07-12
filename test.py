from urllib.parse import quote
from bs4 import BeautifulSoup
import csv
from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.travel-mate.app/'
driver_path = "/home/dolong/Documents/Code/DATN/crawl/hotel/hotel_link/chromedriver"
driver_service = Service(driver_path)
options = webdriver.ChromeOptions()
# options.add_argument('disable-popup-blocking')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(url)
driver.implicitly_wait(10)
# image_element = driver.find_element(By.CLASS_NAME, 'neuYP')
# img_element = image_element.find_element(By.TAG_NAME, "img")

# # # Extract the image link
# image_link = img_element.get_attribute("src")   

# # Get the image link from the "src" attribute
# image_link = image_element.text

# titile = driver.find_element(By.CLASS_NAME, 'EDjsk').find_element(By.CLASS_NAME, 'biGQs').text
# intro = driver.find_element(By.CLASS_NAME, 'EDjsk').find_element(By.CLASS_NAME, 'GYFPJ').text

# do = driver.find_elements(By.CLASS_NAME, 'NSbQk')
# intro = []
# for i in do:
#     if i.find_element(By.CLASS_NAME, 'LNjrQ').text == "Do":
#         x = i.find_elements(By.CLASS_NAME, 'keSJi')
#         for a in x:
#             intro.append(a.text)

# for i in intro:
#     print(i)

with open('test.html', 'w') as f:
    f.write(driver.page_source)