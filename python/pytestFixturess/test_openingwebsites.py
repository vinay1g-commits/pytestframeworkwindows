import pytest


@pytest.mark.usefixtures("setup_teardown")
class TestOpening:
    def test_test1(self):
        self.driver.get("https://www.oneindia.com/")

    def test_test2(self):
        self.driver.get("https://www.filmibeat.com/")

    def test_test3(self):
        self.driver.get("https://www.mykhel.com/")


