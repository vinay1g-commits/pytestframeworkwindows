import time

import pandas
from selenium.webdriver.common.by import By
import pandas as pd
from selenium import webdriver
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/elections/members-of-parliament-list/")
time.sleep(3)
more=driver.find_element(By.ID,"oi-ele-viewmore-btn")
more.location_once_scrolled_into_view
more.click()
politicians_Name=driver.find_elements(By.XPATH,"//div[@class='loksabha-candlist-table']//div//strong")
for val in politicians_Name:
    print(val.get_attribute("strong"))
    som=val.text
    print(som)
with open("politiciansname.txt","r") as file:
    lines=file.readlines()
driver.get("https://www.oneindia.com/politicians/")
for line in lines:
    driver.find_element(By.ID,"search-bar").click()
    driver.find_element(By.ID,"search-bar").send_keys(line)
    time.sleep(2)
    driver.find_element(By.ID,"top_suggestions").click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])

time.sleep(5)
driver.quit()