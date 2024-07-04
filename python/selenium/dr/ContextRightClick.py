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
time.sleep(5)
art1 = driver.find_element(By.XPATH, "(//div[@class='main-block-img'])[1]")
act = ActionChains(driver)
act.context_click(art1).perform()
try:
    # Wait for the pop-up to appear
    pop_up = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='pwa-popup']"))
    )

    # Close the pop-up
    close_button = pop_up.find_element(By.XPATH, "//span[@class='close']")
    close_button.click()
except:
    # If the pop-up does not appear within the timeout, proceed with the rest of the code
    pass
time.sleep(2)
act.send_keys(Keys.CONTROL + 't').perform()
time.sleep(5)
