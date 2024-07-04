import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# To remove automation message from chrome
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.makemytrip.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
time.sleep(2)
fromtxtfld = driver.find_element(By.XPATH,"//span[.='From']")
fromtxtfld.click()
time.sleep(2)
txtfld = driver.find_element(By.XPATH,"//input[@placeholder='From']")
txtfld.send_keys("g")
time.sleep(2)
act = ActionChains(driver)
act.send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
time.sleep(5)