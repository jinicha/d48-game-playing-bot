from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import config

chrome_driver_path = config.chrome_driver_path

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

browser.get("https://www.google.com")
