import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
lang=driver.find_element(By.XPATH,"//span[@class='oi-header-lang-selected']")
lang.click()
sel=Select(lang)
time.sleep(3)
sel.select_by_visible_text("हिन्दी")
sel.select_by_index(6)