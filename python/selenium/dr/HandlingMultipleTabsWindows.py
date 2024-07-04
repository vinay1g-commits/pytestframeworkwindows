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

driver.get("https://www.filmibeat.com/photos/feature/varun-dhawan-sunny-kaushal-avinash-tiwary-other-bollywood-heartthrobs-rocking-summer-style-93958.html")
time.sleep(3)
embed = driver.find_element(By.XPATH,"//button[.='Embed Photo']")
parentWindow = driver.current_window_handle
embed.click()
time.sleep(2)
#driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
print(driver.title)
if driver.title.__eq__("popcorn-admin.greynium.com"):
    time.sleep(2)
    driver.close()

#driver.close()
time.sleep(2)
driver.switch_to.window(parentWindow)
time.sleep(2)
driver.find_element(By.XPATH,"//li[@title='More']").click()
time.sleep(3)
Home = driver.find_element(By.XPATH,"//a[text()='Home']")
bolly = driver.find_element(By.XPATH,"//a[text()='Bollywood ']")
act = ActionChains(driver)
act.key_down(Keys.CONTROL).click(Home).click(bolly).perform()
time.sleep(2)
if driver.current_url.__eq__("https://www.filmibeat.com/bollywood/"):
    time.sleep(2)
    print(driver.current_url)
#driver.switch_to.window(driver.window_handles[2])
time.sleep(2)
"""print(driver.title)
driver.switch_to.window(driver.window_handles[3])
time.sleep(2)
print(driver.title)
"""
time.sleep(3)

