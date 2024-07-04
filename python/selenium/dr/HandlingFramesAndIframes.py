import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
"""driver.get("https://www.oneindia.com/")
time.sleep(5)
driver.switch_to.frame("google_ads_iframe_/1008496/Oneindia-home-728x90_0") #by id

time.sleep(3)
driver.find_element(By.ID,"cbb").click()
#driver.find_element(By.XPATH,"//div[@id='cbb']//*[name()='svg']").click()
time.sleep(3)
driver.switch_to.frame(3)
time.sleep(3)
driver.find_element(By.ID,"cbb").click()
#driver.find_element(By.XPATH,"//div[@id='cbb']//*[name()='svg']").click()
"""
driver.get("https://www.oneindia.com/india/in-focus-pm-modis-best-pics-from-gujarat-poll-campaign-this-year-3493031.html")
time.sleep(5)
slotone=driver.find_element(By.ID,"are-slot-1")
slotone.location_once_scrolled_into_view
time.sleep(2)
print(slotone.get_attribute("data-isloaded"))
print(slotone.get_attribute("data-isbackfill"))
for time in range(7):
    print(slotone.get_attribute("data-google-query-id"))
    sleep(30)

driver.quit()

