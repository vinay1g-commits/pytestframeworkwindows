import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
top_News=driver.find_element(By.XPATH,"//div[@class='oi-heading']//a[@href='/news/']")
top_News.click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
html=driver.page_source
print(html)
driver.quit()