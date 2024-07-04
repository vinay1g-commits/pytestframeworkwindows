import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# To remove automation message from chrome
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.oneindia.com/archives")

# Wait for the Year dropdown to be clickable
year = driver.find_element(By.ID,"archive_year")
year.click()
time.sleep(2)
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//select[@class='archive-select'])[1]")))
drpyear = Select(driver.find_element(By.XPATH, "(//select[@class='archive-select'])[1]"))
drpyear.select_by_visible_text("2022")

# Wait for the month dropdown to be clickable
month = driver.find_element(By.ID, "archive_month")
month.click()
wait2 = WebDriverWait(driver, 5)
wait2.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//select[@class='archive-select'])[2]")))
drpmonth = Select(driver.find_element(By.XPATH, "(//select[@class='archive-select'])[2]"))
drpmonth.select_by_visible_text("May")
time.sleep(2)

# Wait for the day dropdown to be clickable
def remove_disabled_attribute(driver):
    try:
        # Remove "disabled" attribute using XPath
        script = """
        var element = document.evaluate("(//select[@class='archive-select'])[3]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (element) {
            element.removeAttribute("disabled");
        }
        """
        driver.execute_script(script)
    except NoSuchElementException:
        print("Element with XPath '(//select[@class='archive-select'])[3]' not found.")

remove_disabled_attribute(driver)
time.sleep(2)
day = driver.find_element(By.XPATH, "(//select[@class='archive-select'])[3]")
day.click()
time.sleep(2)
drpday = Select(driver.find_element(By.XPATH,"(//select[@class='archive-select'])[3]"))
drpday.select_by_visible_text("01")
time.sleep(2)
driver.refresh()

# Optional sleep for demonstration
time.sleep(3)

# Close the browser
driver.quit()
