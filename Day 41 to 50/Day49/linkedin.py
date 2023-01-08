from selenium import webdriver
from selenium.webdriver import Keys

# setup selenium
windows_driver_path = "H:/100DaysPY/Day41 to 50/Day 46/windows-driver/msedgedriver.exe"
driver = webdriver.Edge(executable_path=windows_driver_path)
driver.get("https://www.linkedin.com/")

# login
email_in = driver.find_element("id", "session_key")
email_in.send_keys("")
pass_input = driver.find_element("id", "session_password")
pass_input.send_keys("")
login_button = driver.find_element("xpath", '//*[@id="main-content"]/section[1]/div/div/form/button')
login_button.send_keys(Keys.ENTER)
driver.set_page_load_timeout(100)
job_search_url = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer' \
                 '&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0 '
driver.get(job_search_url)

jobs = driver.find_elements(by="css selector", value=".job-card-container div div a")
for job in jobs:
    job.click()
    submit_button = driver.find_element("css selector", ".jobs-s-apply .jobs-apply-button--top-card .jobs-apply-button")
    print(submit_button.text)
    submit_button.click()
    next_button = driver.find_element("id", "ember371")
    next_button.click()

    # it works.
