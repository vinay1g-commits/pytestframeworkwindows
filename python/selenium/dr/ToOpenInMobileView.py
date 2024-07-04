import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Define mobile user agent
user_agent = ("Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/116.0.0.0 Mobile Safari/537.36")

# Set chrome options
opt = Options()
opt.add_argument(f'user-agent={user_agent}')
opt.add_argument('--window-size=360,1000')  # Set window size for mobile view
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-dev-shm-usage')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")

# Start the Chrome browser with the specified options
driver = webdriver.Chrome(options=opt)

# Open the website
driver.get('https://www.oneindia.com/')
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

