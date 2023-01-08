from selenium import webdriver
from selenium.webdriver import Keys

# setup selenium
windows_driver_path = "H:/100DaysPY/Day41 to 50/Day 46/windows-driver/msedgedriver.exe"
driver = webdriver.Edge(executable_path=windows_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")
lang = driver.find_element(by="id", value="#promptContent .langSelectButton")
print(lang.text)
#
# button = driver.find_element(by="id", value="bigCookie")
# for i in range(0, 101):
#     button.click()