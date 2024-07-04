from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
ele=driver.find_element(By.TAG_NAME,"a")
print(ele.get_attribute("href"))
print("============================================")
eles=driver.find_elements(By.TAG_NAME,"a")
for l in eles:
    print(l.get_attribute("href"))

driver.quit()
