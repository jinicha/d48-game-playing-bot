from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import threading
import config

chrome_driver_path = config.chrome_driver_path

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

browser.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = browser.find_element(By.ID, "cookie")
money = browser.find_element(By.ID, "money")
products = browser.find_elements(By.CSS_SELECTOR, "#rightPanel b")[:-1]
all_products = [p.text.split("-")[0].strip() for p in products]
prices = [p.text.split("-")[1].strip() for p in products]
grayed_products = browser.find_elements(By.CSS_SELECTOR, ".grayed b")
not_available_products = [p.text.split("-")[0].strip() for p in grayed_products]


def check_upgrade():
    threading.Timer(5.0, check_upgrade).start()
    available_product = [p for p in all_products if p not in not_available_products]
    if len(available_product) > 0:
        buy = available_product[-1]
        buy_product = browser.find_element(By.ID, f'buy{buy}')
        buy_product.click()


timeout = time.time() + 60*5
while True:
    test = 0
    if test == 5 or time.time() > timeout:
        break

    cookie.click()
    check_upgrade()
    test = test - 1
