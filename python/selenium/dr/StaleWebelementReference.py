import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
time.sleep(3)
searchbtn=driver.find_element(By.XPATH,"//div[@class='oi-header-searchblock']")
searchbtn.click()
time.sleep(2)
searchBox=driver.find_element(By.ID,"oneindia_search")
time.sleep(2)
searchBox.send_keys("news")
time.sleep(2)
searchBox.send_keys(Keys.ENTER)
time.sleep(3)
driver.back()
#Now all the referenced object storing elements ID,Xpath etc will be vanished so solution is dont store in menmory and reference via object
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='oi-header-searchblock']").click()
time.sleep(2)
driver.find_element(By.ID,"oneindia_search").send_keys("news")
time.sleep(2)
driver.find_element(By.ID,"oneindia_search").send_keys(Keys.ENTER)
time.sleep(2)
#driver.quit()
