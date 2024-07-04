import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
driver.fullscreen_window()
time.sleep(3)
if driver.find_element(By.XPATH,"(//i[@class='option-selected'])[1]").is_selected():
    print("its in selected state")
else:
    print("not in selected state")
driver.quit()