import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://testpages.eviltester.com/styled/index.html")
driver.find_element(By.ID,"alerttest").click()
time.sleep(2)
info_alert_box=driver.find_element(By.ID,"alertexamples")
info_alert_box.click()
time.sleep(2)
switching=driver.switch_to.alert
time.sleep(2)
print(switching.text)
switching.accept()
time.sleep(2)
#driver.switch_to.window()
#time.sleep(2)
#confirm_alert=driver.find_element(By.ID,"confirmexample")
#confirm_alert.click()
#confirm_alert.submit()

driver.quit()