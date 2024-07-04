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

driver.get("https://www.oneindia.com/india/")
time.sleep(3)

# Define the XPath for the "Next" button
next_button_xpath = "//a[@class='oi-city-next']"

# Loop until the desired text is found
while True:
    containerNws = driver.find_elements(By.XPATH, "//div[@class='oi-cityblock-list']//li//a")
    for element in containerNws:
        if element.text == 'Nitish Kumar Goofs Up Again, Says May Narendra Modi Become "Chief Minister" | Watch Video':
            link_href = element.get_attribute("href")
            print(link_href)
            # If found, exit the loop
            driver.quit()
            break

    # If the desired text is not found, click on the "Next" button
    next_button = driver.find_element(By.XPATH, next_button_xpath)
    if next_button.is_enabled():
        next_button.click()
        time.sleep(3)  # Wait for the page to load
    else:
        # If the "Next" button is disabled, exit the loop
        print("Desired text not found")
        driver.quit()
        break
