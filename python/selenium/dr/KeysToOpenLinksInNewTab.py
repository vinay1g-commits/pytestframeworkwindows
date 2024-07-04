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
News = driver.find_elements(By.XPATH, "(//li[@class='mainclass'])[1]")
NewsSubLinks = driver.find_elements(By.XPATH, "//div[@class='oi-nav-block subnav']/ul//li//a[@href]")
for links in NewsSubLinks:
    #act = ActionChains(driver)
    #act.key_down(Keys.CONTROL).click(links).key_up(Keys.CONTROL).perform()
    driver.execute_script("window.open(arguments[0], '_blank');", links.get_attribute("href"))

time.sleep(5)
driver.quit()
