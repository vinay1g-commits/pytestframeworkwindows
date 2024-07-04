from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.w3schools.com/bootstrap/bootstrap_modal.asp")
dialogBox=driver.find_element(By.XPATH,"//button[.='Click To Open Modal']" )
dialogBox.click()
driver.find_element(By.XPATH,"//button[.='Close']").click()
driver.quit()