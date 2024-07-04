import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def setup_teardown(request):
    opt = Options()
    opt.add_experimental_option("excludeSwitches", ["enable-automation"])
    opt.add_experimental_option("useAutomationExtension", False)
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opt)
    request.cls.driver = driver
    yield
    time.sleep(2)
    driver.quit()
