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

driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.find_element(By.ID, 'datepicker').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))

def calendar(month, year, day):
    while True:
        # Get the current month and year displayed on the calendar
        current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

        # Check if the current month and year match the desired month and year
        if current_month == month and current_year == year:
            break  # Exit the loop if the desired month and year are found

        # Click the "Next" button to navigate to the next month
        driver.find_element(By.XPATH, "//span[text()='Next']").click()

    # Click on the desired day
    driver.find_element(By.XPATH, f"//a[text()='{day}']").click()

calendar('May', '2024', '1')

time.sleep(3)
driver.quit()


#daysof = ("//td[@data-handler='selectDay']/a[text()='" + str(da) + "']")
