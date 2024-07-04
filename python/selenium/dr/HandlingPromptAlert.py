import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://testpages.eviltester.com/styled/index.html")
driver.find_element(By.ID,"alerttest").click()
time.sleep(2)
promptAlert=driver.find_element(By.ID,"promptexample")
promptAlert.click()
switchToPromptAlert=driver.switch_to.alert
print(switchToPromptAlert.text)
switchToPromptAlert.send_keys("vinay")
time.sleep(2)
switchToPromptAlert.accept()
time.sleep(1)
time.sleep(2)
driver.quit()