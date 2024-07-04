import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options=Options()
firefox_options.add_argument('--disable-notifications')
driver=webdriver.Firefox(options=firefox_options)
driver.maximize_window()
driver.get("https://www.homedepot.com/")
time.sleep(15)
driver.quit()
