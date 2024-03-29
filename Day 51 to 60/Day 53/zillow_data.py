import time

import selenium
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import Keys

# setup selenium
windows_driver_path = "H:/100DaysPY/Day41 to 50/Day 46/windows-driver/msedgedriver.exe"
driver = webdriver.Edge(executable_path=windows_driver_path)
# constants
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C' \
             '%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A' \
             '-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C' \
             '%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A' \
             '%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse' \
             '%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B' \
             '%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D' \
             '%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min' \
             '%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D '

# web scarping using selenium
driver.get(ZILLOW_URL)
html_element = driver.find_element("tag name", 'body')
html_element.send_keys(Keys.END)
print("end")

prices = driver.find_elements("css selector", ".kJFQQX")
for item in prices:
    print(item.text)