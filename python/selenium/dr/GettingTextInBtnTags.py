import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
time.sleep(3)
texto = driver.find_element(By.XPATH,"//div[@id='toptextpromo']//following::div[1]").text
print(texto)
texto2=driver.find_element(By.XPATH,"//a[@href='/videos/']").text
print(texto2)