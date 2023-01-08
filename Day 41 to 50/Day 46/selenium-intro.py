from selenium import webdriver

# setup selenium
windows_driver_path = "H:/100DaysPY/Day41 to 50/Day 46/windows-driver/msedgedriver.exe"
driver = webdriver.Edge(executable_path=windows_driver_path)

# getting

names = []
dates_l1 = []
result = {}
index = 1
driver.get("https://www.python.org/")
for date in driver.find_elements(by="css selector", value='div section div div div ul li time')[-1:-6:-1]:
    dates_l1.append(date.text)
for i in range(1, 6):
    for event_name in driver.find_elements(by="xpath",
                                           value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a'):
        names.append(event_name.text)


dates = [date for date in dates_l1[::-1]]
for i in range(0, len(dates)):
    result[str(i)] = {'date': dates[i],
                      'name': names[i]}

print(result)
driver.close()  # will close the active window
driver.quit()  # this will close the active tab
