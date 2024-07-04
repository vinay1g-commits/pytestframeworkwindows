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

driver.get("https://www.oneindia.com/")
time.sleep(3)
driver.save_screenshot("cvb.png")
searchbtn = driver.find_element(By.XPATH,"//div[@class='oi-header-search os-header-rt-search-b']")
searchbtn.click()
time.sleep(2)
searchbtn.screenshot("btn.png")
time.sleep(2)
driver.save_screenshot("qwe.png")
time.sleep(2)
act = ActionChains(driver)
text_box = driver.find_element(By.ID,"oneindia_search")
act.click(text_box).pause(2).send_keys("news").pause(2).send_keys(Keys.ENTER).perform()
time.sleep(3)
driver.save_screenshot("ggg.png")
time.sleep(3)
driver.get_screenshot_as_file("lala.png")
time.sleep(3)
resultpg = driver.find_element(By.XPATH,"//div[@class='gsc-resultsbox-visible']")
resultpg.screenshot("section.png")
time.sleep(3)
