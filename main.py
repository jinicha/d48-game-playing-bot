from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import config

chrome_driver_path = config.chrome_driver_path

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

browser.get("https://www.python.org/")
response = browser.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = response[0].text.split("\n")
events_time = [e for e in events if events.index(e) % 2 == 0]
events_title = [e for e in events if events.index(e) % 2 != 0]
events_dict = {}
for index, time in enumerate(events_time):
    events_dict[index] = {
        "time": time,
        "name": events_title[index]
    }

print(events_dict)

browser.quit()
