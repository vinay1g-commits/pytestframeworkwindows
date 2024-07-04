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

driver.get("https://www.oneindia.com/photos/")
time.sleep(2)
photo1 = driver.find_element(By.XPATH,"(//div[@class='oi-photos-image'])[1]")
photo2 = driver.find_element(By.XPATH,"(//div[@class='oi-photos-image'])[5]")
act = ActionChains(driver)
act.click_and_hold(photo1).move_to_element(photo2).release().perform()
time.sleep(3)
driver.get("https://www.w3schools.com/HTML/html5_draganddrop.asp")
time.sleep(3)
drag = driver.find_element(By.ID,"drag1")
drop = driver.find_element(By.ID,"div2")
#drag.location_once_scrolled_into_view
time.sleep(2)
act.drag_and_drop(drag,drop).perform()
time.sleep(3)
