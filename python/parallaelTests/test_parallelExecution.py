import time
from selenium import webdriver


def test_test1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.oneindia.com/")
    time.sleep(2)
    driver.quit()

def test_test2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.filmibeat.com/")
    time.sleep(2)
    driver.quit()

def test_test3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.mykhel.com/")
    time.sleep(2)
    driver.quit()
