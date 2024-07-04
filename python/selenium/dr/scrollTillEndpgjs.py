import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.oneindia.com/archives/")
time.sleep(3)

driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(3)

input("press enter to close the browser")
driver.quit()
