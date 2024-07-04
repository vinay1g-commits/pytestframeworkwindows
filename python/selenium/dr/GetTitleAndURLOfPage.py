from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
title1=driver.title
print(title1)
url1 = driver.current_url
print(url1)
weather=driver.find_element(By.XPATH,"//p[.='Weather Today']")
weather.click()
title2=driver.title
print(title2)
url2=driver.current_url
print(url2)
driver.quit()