import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# To remove automation message from chrome
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get('https://www.oneindia.com/politicians/')
driver.implicitly_wait(10)

stateDrpDn = driver.find_element(By.XPATH, "(//span[text()='Select State'])[2]")
stateDrpDn.click()

listStates = driver.find_elements(By.XPATH, "//ul[@id='state_suggestions']//li")

for state in listStates:
    # Get the URL of the state
    state_url = state.find_element(By.XPATH, ".//a").get_attribute("href")
    # Open the state URL in a new tab using JavaScript
    driver.execute_script("window.open(arguments[0]);", state_url)
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)  # Optional: Add a delay to allow the page to load
    # Perform any actions you want in the new tab
    # For now, I'll just print the page title
    print(driver.title)
    # Close the current tab (optional)
    driver.close()
    # Switch back to the main tab
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)  # Optional: Add a delay before opening the next state

driver.quit()
