import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# To remove automation message from chrome
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.oneindia.com/archives/")
time.sleep(3)
#driver.execute_script("document.getElementById('archive_year').click")
#document.getElementsByClassName('archive-select')[0].click()
#document.getElementById('archive_year')
#document.getElementsByTagName('option')[0]
#document.getElementsByTagName('td')[0].innerHTML
#document.getElementById('archive_year').id
#document.title
#document.URL
#document.getElementsByClassName('oi-header-search os-header-rt-search-b').valueOf('news')
#document.getElementById('archive_year').style.color='red'
# nothing works below: 
"""year = driver.find_element(By.ID, "archive_year")
driver.execute_script("arguments[0].click();", year)
year2 = driver.find_element(By.ID, "archive_year")
driver.execute_script("arguments[0].value = '2023';", year2)"""
year3 = driver.find_element(By.ID, "archive_year")
value = driver.execute_script("return arguments[0].getAttribute('value');", year3)
print(value)

time.sleep(3)
driver.quit()