from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.oneindia.com/")
time.sleep(3)
height = driver.execute_script("return Math.max("
    "document.body.scrollHeight, document.body.offsetHeight, "
    "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
    "document.documentElement.offsetHeight)")
width = driver.execute_script("return Math.max("
    "document.body.scrollWidth, document.body.offsetWidth, "
    "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
    "document.documentElement.offsetWidth)")
print(height, width)
