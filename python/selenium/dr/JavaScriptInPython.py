import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# To remove automation message from chrome
opt = Options() 
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.oneindia.com/")
time.sleep(3)
driver.execute_script("alert('ATTENTION YOUR WEBSITE IS NOT SECURE ANYMORE')")
time.sleep(3)
