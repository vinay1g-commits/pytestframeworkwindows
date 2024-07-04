import time
from selenium import webdriver

"""def setup_function(function): # this will make it(setup and teardown function) run before and after every test method in the directory.
    print("launch browser")

def teardown_function(function):
    print("close browser")
"""

def setup_module(module): # this  will make it(setup) run once before running all test method in the directory and then towards the end it will run teardown code.
    print("launch browser")

def teardown_module(module):
    print("close browser")

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
