
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)


driver.get("https://www.oneindia.com/india/centre-starts-granting-citizenship-under-caa-in-bengal-haryana-uttarakhand-3837123.html")
time.sleep(3)
text = str(driver.execute_script("return document.documentElement.innerText"))
print(text)

input("press enter")
driver.quit()