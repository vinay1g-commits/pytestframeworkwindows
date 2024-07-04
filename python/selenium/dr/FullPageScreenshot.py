from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--headless')  # Add this line to run in headless mode
driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.oneindia.com/")
time.sleep(5)
height = driver.execute_script("return Math.max("
    "document.body.scrollHeight, document.body.offsetHeight, "
    "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
    "document.documentElement.offsetHeight)")
width = driver.execute_script("return Math.max("
    "document.body.scrollWidth, document.body.offsetWidth, "
    "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
    "document.documentElement.offsetWidth)")
print(height, width)

driver.set_window_size(width,height)
time.sleep(5)
body = driver.find_element(By.TAG_NAME,"body")
body.screenshot("fulloo.png")