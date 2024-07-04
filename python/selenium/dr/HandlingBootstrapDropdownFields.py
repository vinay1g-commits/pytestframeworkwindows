import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/lok-sabha-elections/")
time.sleep(3)
states=driver.find_element(By.XPATH,"(//span[@class='oi-level-selstate'])[1]")
states.location_once_scrolled_into_view
time.sleep(2)
states.click()
driver.find_element(By.XPATH,"//div[@id='pcState']/descendant::li//a[.='Jharkhand ']").click()
time.sleep(2)
driver.quit()