import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
class TestAssertion:
    def test_assertio(self):
        self.driver.get("https://www.oneindia.com/")
        time.sleep(3)
        actual_title = self.driver.title
        expected_title = "News, Latest News, Today's News Headlines, Breaking News, LIVE News - Oneindia"
        assert actual_title.__eq__(expected_title)
        self.driver.find_element(By.XPATH, "//div[@class='oi-header-searchblock']").click()
        placeholder = self.driver.find_element(By.XPATH, "//input[@placeholder='Search Latest News, Photos, Videos']")
        assert placeholder.is_displayed()
        time.sleep(3)
