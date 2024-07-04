import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.set_page_load_timeout(5)
driver.get("https://www.oneindia.com/")
time.sleep(3)
driver.quit()