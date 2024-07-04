import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# To remove automation message from chrome
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.oneindia.com/")
time.sleep(5)
#block = driver.find_element(By.XPATH,"//div[@class='oi-container margin-bottom clearfix']")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='oi-container margin-bottom clearfix']")))
articles = "//ul[@id='hp-top-news-middle']/child::li"
arti = "//ul[@id='hp-top-news-middle']/child::li//a"
listings = driver.find_elements(By.XPATH,articles)
for list in listings:
    print(list.text)

listings2 = driver.find_elements(By.XPATH,arti)
for list2 in listings2:
    href = list2.get_attribute("href")
    # href = list.find_elements(By.XPATH,"./a").__getattribute__("href")
    print(href)




time.sleep(5)

