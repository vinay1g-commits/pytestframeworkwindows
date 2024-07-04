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
driver.get("https://www.oneindia.com")
# To move cursor to an element
time.sleep(5)
act = ActionChains(driver)
ele1 = driver.find_element(By.XPATH, "//a[.=' News ']")
ele2 = driver.find_element(By.XPATH,"//span[.='Sports']")
act.move_to_element(ele1).perform()
time.sleep(2)
act.click(ele2).perform()
time.sleep(5)
driver.quit()
