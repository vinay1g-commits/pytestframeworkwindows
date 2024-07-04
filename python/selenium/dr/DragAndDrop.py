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

driver.get("https://www.goodreturns.in/sip-calculator.html")
time.sleep(3)

loc = driver.find_element(By.ID,"investment_button")
MI = driver.find_element(By.ID,"invest_amt_range")
loc.location_once_scrolled_into_view
time.sleep(2)

slider_width = MI.size['width']
act = ActionChains(driver)
#act.drag_and_drop_by_offset(MI,-slider_width,0).perform()
act.move_to_element(MI).click_and_hold().move_by_offset(-slider_width, 0).release().perform()
time.sleep(2)
act.move_to_element(MI).click_and_hold().move_by_offset(1,0).release().perform()

time.sleep(5)
driver.quit()