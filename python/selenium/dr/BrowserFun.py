import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
time.sleep(3)
#driver.find_element(By.CLASS_NAME,"more").click()
#driver.find_element(By.XPATH,"//p[.='Weather Today']").click()
#driver.find_element(By.LINK_TEXT,'বাংলা').click()
driver.find_element(By.CLASS_NAME,'oi-header-searchblock').click()
searchBtn = driver.find_element(By.ID,'oneindia_search')
searchBtn.send_keys("news")
searchBtn.clear()