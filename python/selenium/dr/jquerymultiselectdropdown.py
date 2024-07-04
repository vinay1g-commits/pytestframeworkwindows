import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.find_element(By.ID,"justAnInputBox").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//span[contains(text(),'choice 2')])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//span[contains(text(),'choice 6 1')])[1]").click()
time.sleep(2)
driver.quit()
