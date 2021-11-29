from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import config

chrome_driver_path = config.chrome_driver_path

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

browser.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = browser.find_element(By.ID, "cookie")
products = browser.find_elements(By.CSS_SELECTOR, "#rightPanel b")[:-1]
all_products = [p.text.split("-")[0].strip() for p in products]

five_sec = time.time() + 5
five_min = time.time() + 60*2

while True:
    cookie.click()
    if time.time() > five_sec:
        grayed_products = browser.find_elements(By.CSS_SELECTOR, ".grayed b")
        not_available_products = [p.text.split("-")[0].strip() for p in grayed_products]
        available_products = [p for p in all_products if p not in not_available_products]
        print("available products: ", available_products)
        if len(available_products) > 0:
            buy = available_products[-1]
            buy_product = browser.find_element(By.ID, f'buy{buy}')
            buy_product.click()
            print(f'just bought {buy}')

        five_sec = time.time() + 5

    if time.time() > five_min:
        cookie_per_sec = browser.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break
