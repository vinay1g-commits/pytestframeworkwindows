import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
time.sleep(3)
poll=driver.find_element(By.ID,"question_mode_container_41708")
poll.location_once_scrolled_into_view
polloption=driver.find_element(By.XPATH,"(//div[@class='poll-option-details']/ul/li)[3]")
if polloption.is_selected():
    pass
else:
    polloption.click()
time.sleep(3)
driver.quit()