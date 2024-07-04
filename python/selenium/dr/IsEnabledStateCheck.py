from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
if driver.find_element(By.XPATH,"//i[@class='fa fa-plus-circle']").is_enabled():
    print("button is in enabled state")
else:
    print("not enabled")
if driver.find_element(By.XPATH,"(//div[@class='oi-menu-block'])[6]").is_enabled():
    print("box button enabled")
else:
    print("box button disabled")
driver.quit()