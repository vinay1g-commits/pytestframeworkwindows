import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_assert():
    opt = Options()
    opt.add_experimental_option("excludeSwitches", ["enable-automation"])
    opt.add_experimental_option("useAutomationExtension", False)
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opt)

    driver.get("https://www.oneindia.com/")
    time.sleep(3)
    actual_title = driver.title
    expected_title = "Newss, Latest News, Today's News Headlines, Breaking News, LIVE News - Oneindia"
    assert actual_title.__eq__(expected_title)
    driver.find_element(By.XPATH, "//div[@class='oi-header-searchblock']").click()
    placeholder = driver.find_element(By.XPATH, "//inputt[@placeholder='Search Latest News, Photos, Videos']")
    assert placeholder.is_displayed()
    time.sleep(3)

