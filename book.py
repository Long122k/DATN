import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium webdriver
driver_path = "/home/dolong/Documents/chromedriver_linux64/chromedriver"
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(service=Service(driver_path), options=options)
driver.implicitly_wait(10)

with open('crawl/hotel/tripAdvisor/country/link_country.csv', 'r') as file:
    
# url = "https://www.tripadvisor.com/Hotels-g293921-Vietnam-Hotels.html"
url = 'https://www.tripadvisor.com/Hotels-g293921-oa300-Vietnam-Hotels.html'

# Open the URL in the Selenium webdriver
driver.get(url)

# while True:
    # print(url)

    # Get the page source after the JavaScript has rendered the content
page_source = driver.page_source
# print(page_source)
with open('./test3.html', 'w') as file:
    file.write(page_source)
# Create a BeautifulSoup object with the page source
soup = BeautifulSoup(page_source, "html.parser")

# Find the <a> tag with class "property_title prominent"
a_tags = soup.find_all("a", class_="property_title prominent")

# Extract the href attribute value
for a_tag in a_tags:
    href = a_tag.get("href")
    print(href)

# # Find the "Next" button element using XPath
    # next_button = driver.find_element(By.XPATH, '//span[@class="nav next ui_button primary"]')
    # time.sleep(20)
    # print("Element is visible? " + str(next_button.is_displayed()))
    # print(next_button)
    # next_button.click()
    # print("clicked")
    # Check if the "Next" button is present
    # if next_button:
    #     # Click the "Next" button
    #     next_button.click()
    #     print("clicked")


    #     # Wait for the new page to load
    #     WebDriverWait(driver, 10).until(EC.staleness_of(next_button))
    #     time.sleep(2)  # Optional: Add a small delay to ensure the page has fully loaded
    # else:
    #     break
    # Find the "Next" button element
    # next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[32]/div/div/div[1]/div[2]/div')
    # print(next_button.is_displayed())
    # # Extract the URL from the "Next" button
    # next_page_url = next_button.get_attribute("onclick").split(",")[-1].strip("'")
    # next_page_url = 'https://www.tripadvisor.com/Hotels-g293921-oa30-Vietnam-Hotels.html'
    # # Navigate to the next page URL
    # driver.get(next_page_url)
# Close the Selenium webdriver
driver.quit()
