from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import config

chrome_driver_path = config.chrome_driver_path

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

browser.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = browser.find_element(By.ID, "cookie")
while True:
    cookie.click()
