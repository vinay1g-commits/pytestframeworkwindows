from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

"""chrome_driver_path = "D:\\chromedriver\\chromedriver-win64\\chromedriver.exe"
service = Service(chrome_driver_path)
service.start()
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
driver.maximize_window()
"""
opt = Options()
opt.add_experimental_option("excludeSwitches",["enable-automation"])
opt.add_experimental_option("useAutomationExtension",False)
opt.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=opt)
driver.get("https://www.google.com")
driver.maximize_window()

print(driver.title)
# Add a delay to keep the browser open for a few seconds
import time
time.sleep(15)