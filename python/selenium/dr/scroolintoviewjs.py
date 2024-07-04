import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.oneindia.com/archives/")
time.sleep(3)
scroll_till = driver.find_element(By.XPATH,"//a[.='2006']")
driver.execute_script("arguments[0].scrollIntoView();",scroll_till)
#scroll_till.location_once_scrolled_into_view
time.sleep(3)
driver.quit()
