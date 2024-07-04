import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
time.sleep(3)
search_Btn=driver.find_element(By.XPATH,"//div[@class='oi-header-searchblock']")
search_Btn.click()
text_Box=driver.find_element(By.XPATH,"//input[@id='oneindia_search']")
text_Box.send_keys("news")
time.sleep(2)
text_Box.click()
time.sleep(2)
text_Box.submit()
time.sleep(2)
driver.quit()