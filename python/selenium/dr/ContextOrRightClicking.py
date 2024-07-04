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

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(3)
btn = driver.find_element(By.XPATH,"//span[text()='right click me']")
act = ActionChains(driver)
act.context_click(btn).perform()
time.sleep(2)
quit_option = driver.find_element(By.XPATH,"//li/span[text()='Quit']")
act.click(quit_option).perform()
time.sleep(3)


