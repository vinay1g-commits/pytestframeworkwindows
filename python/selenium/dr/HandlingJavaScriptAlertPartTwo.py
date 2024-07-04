import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://testpages.eviltester.com/styled/index.html")
driver.find_element(By.ID,"alerttest").click()
time.sleep(2)
cnfrm_alert_box=driver.find_element(By.ID,"confirmexample")
cnfrm_alert_box.click()
switching_cnfrm_alert=driver.switch_to.alert
print(switching_cnfrm_alert.text)
switching_cnfrm_alert.dismiss()
time.sleep(2)
driver.quit()