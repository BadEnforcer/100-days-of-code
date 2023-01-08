from selenium import webdriver
from selenium.webdriver import Keys

# setup selenium
windows_driver_path = "H:/100DaysPY/Day41 to 50/Day 46/windows-driver/msedgedriver.exe"
driver = webdriver.Edge(executable_path=windows_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# stat = driver.find_element(by="css selector", value="#articlecount a")
# print(stat.text)
# # clicking on templates
# link = driver.find_element(by="link text", value="English")
# link.click()  # click
#
# # input a value
# search = driver.find_element(by="name", value="search")  # get hold of search bar
# search.send_keys("python")  # sends the value to in the input field
# search.send_keys(Keys.ENTER)  # send the enter key

# TEST 1 ::
driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(by="name", value="fName")
f_name.send_keys("Raj")
l_name = driver.find_element(by="name", value="lName")
l_name.send_keys("Dwivedi")
email = driver.find_element(by="name", value="email")
email.send_keys("name@gmail.com")
button = driver.find_element(by="css selector", value="form button")
button.send_keys(Keys.ENTER)


