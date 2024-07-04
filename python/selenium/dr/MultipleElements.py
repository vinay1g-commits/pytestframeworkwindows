from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
links=driver.find_elements(By.XPATH,"//a")
print(len(links))
for l in links:
    print(l.get_attribute("href"))

driver.get("https://www.oneindia.com/lok-sabha-elections/")
constituencies=driver.find_elements(By.XPATH,"(//div[@class='election-db__search-block leader'])[2]//following::li//a")
print(len(constituencies))
for c in constituencies:
    print(c.get_attribute("title"))
    print(c.text)


driver.quit()