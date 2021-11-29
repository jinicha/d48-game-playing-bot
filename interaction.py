from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import config

chrome_driver_path = config.chrome_driver_path

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

# WIKIPEDIA CHALLENGE
browser.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = browser.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

browser.quit()
