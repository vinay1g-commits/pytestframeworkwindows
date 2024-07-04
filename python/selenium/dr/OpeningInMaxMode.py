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
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)
#driver.maximize_window()

#using Keys Class
driver.get("https://www.oneindia.com/")
time.sleep(3)
act = ActionChains(driver)
accnt = driver.find_element(By.ID,"userSignedin")
act.click(accnt).perform()
time.sleep(2)
contnwg = driver.find_element(By.XPATH,"//img[@alt='Sign in with Google']")
act.click(contnwg).perform()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
email = (driver.find_element(By.ID,"identifierId"))
act.pause(10).send_keys("vinay1g19").perform()
time.sleep(2)
act.send_keys(Keys.ENTER).perform()
time.sleep(2)
# to write same line of commands in multiple lines use \