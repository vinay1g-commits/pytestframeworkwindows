import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sweetalert2.github.io/")
time.sleep(2)
btn = driver.find_element(By.XPATH,"//button[text()='Show normal alert']")
btn.click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.alert_is_present())

swtchal = driver.switch_to.alert
print(swtchal.text)
swtchal.accept()
time.sleep(2)