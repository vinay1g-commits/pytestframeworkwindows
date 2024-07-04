import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# To remove automation message from chrome
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.oneindia.com/")
time.sleep(2)
morebtn = driver.find_element(By.XPATH, "//a[@class='more']")
act = ActionChains(driver)
act.double_click(morebtn)
print("doubled clicked")
time.sleep(5)
