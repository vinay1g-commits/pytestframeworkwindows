from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Set the mobile emulation options
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"
}

# Set Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode, comment out this line to run with GUI
firefox_options.add_argument("--width=360")  # Set window width
firefox_options.add_argument("--height=640")  # Set window height
firefox_options.add_argument(f"user-agent={mobile_emulation['userAgent']}")  # Set user agent

# Create a Firefox webdriver with the specified options
driver = webdriver.Firefox(options=firefox_options)

# Navigate to a website to test the mobile view
driver.get("https://www.oneindia.com")

# Optional: Print page title to verify
print("Page title:", driver.title)

# Optional: Take a screenshot to verify the mobile view
driver.save_screenshot("mobile_view_screenshot.png")

# Close the browser
driver.quit()
