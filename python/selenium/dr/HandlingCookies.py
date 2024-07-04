import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://stackoverflow.com/")
time.sleep(3)
window_google=driver.find_element(By.XPATH,"//div[@id='animated-container']")
switch =  driver.switch_to.window(window_google)
switch.accept()
time.sleep(2)
driver.find_element(By.ID,"onetrust-reject-all-handler").click()
driver.quit()