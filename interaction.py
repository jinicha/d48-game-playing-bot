from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import config

chrome_driver_path = config.chrome_driver_path

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

# FILLING FORM CHALLENGE
browser.get("http://secure-retreat-92358.herokuapp.com/")
first_name = browser.find_element(By.NAME, "fName")
first_name.send_keys("Jini")
last_name = browser.find_element(By.NAME, "lName")
last_name.send_keys("C")
email = browser.find_element(By.NAME, "email")
email.send_keys("test100daysofpython@gmail.com")
sign_up_button = browser.find_element(By.TAG_NAME, "button")
sign_up_button.click()

# WIKIPEDIA CHALLENGE
# browser.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = browser.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# browser.quit()
