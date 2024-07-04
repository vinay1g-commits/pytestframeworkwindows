import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.oneindia.com/")
time.sleep(3)

# Define the target element to scroll until it's no longer visible
scroll_step = 1000  # Adjust scroll step as needed

# Scroll down to the bottom of the page
while True:
    # Scroll down by scroll_step pixels
    driver.execute_script("window.scrollBy(0, {});".format(scroll_step))
    time.sleep(2)  # Adjust sleep time as needed

    # Check if the page has reached the bottom
    is_bottom = driver.execute_script(
        "return window.innerHeight + window.pageYOffset >= document.body.scrollHeight"
    )
    if is_bottom:
        # Scroll back to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
        break

# Close the browser
driver.quit()
