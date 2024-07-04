from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
if driver.find_element(By.XPATH,"(//div[@class='oi-header-logo'])[1]").is_displayed():
    print("element is displayed in the page")
else:
    print("element is not displayed in the page")

if driver.find_element(By.ID,"lang_id").is_displayed():
    print("hidden element is displayed in the page")
else:
    print("hidden element is not displayed in the page")
driver.quit()