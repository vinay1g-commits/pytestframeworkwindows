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

driver.get("https://jqueryui.com/resizable/")
time.sleep(2)
frame = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)
time.sleep(2)
resizableBar = driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-e']")
act = ActionChains(driver)
act.drag_and_drop_by_offset(resizableBar,60,130).perform()
time.sleep(3)