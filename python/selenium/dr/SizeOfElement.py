from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
ele=driver.find_element(By.XPATH,"//*[@class='3805221']").size
print(ele)

driver.quit()