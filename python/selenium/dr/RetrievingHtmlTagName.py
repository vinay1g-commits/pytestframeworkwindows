from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
some=driver.find_element(By.XPATH,"//*[@class='3801821']")
print(some.tag_name)
driver.quit()