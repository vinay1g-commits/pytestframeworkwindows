import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# To remove automation message from chrome
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.oneindia.com/")
time.sleep(3)
driver.execute_script('alert("hi howady")')
alert = driver.switch_to.alert
alert.accept()

time.sleep(2)
driver.execute_script('prompt("enter your gender maann")')
alert.accept()
time.sleep(2)
driver.execute_script('confirm("ARE YOU NOT SURE?WHY?")')
alert.accept()
time.sleep(2)




#alert("hi howady")
#prompt("enter your gender maann")
#confirm("ARE YOU NOT SURE?WHY?")