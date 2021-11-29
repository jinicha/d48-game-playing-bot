from selenium import webdriver
import config

chrome_driver_path = config.chrome_driver_path

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.google.com")
