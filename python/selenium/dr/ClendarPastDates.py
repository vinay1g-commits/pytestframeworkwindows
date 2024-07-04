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

driver.find_element(By.ID,"datepicker").click()

wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.ID,"ui-datepicker-div")))

def calendarprev(driver,month,year,day):
    currmonth = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']")
    curryear = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']")
    while not(currmonth.text.__eq__(month) and curryear.text.__eq__(year)):
        driver.find_element(By.XPATH,"//span[.='Prev']").click()
        currmonth = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']")
        curryear = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']")
    driver.find_element(By.XPATH,"//a[@class='ui-state-default'][.='"+str(day)+"']").click()

calendarprev(driver,"August","2022","1")
time.sleep(5)
driver.quit()

