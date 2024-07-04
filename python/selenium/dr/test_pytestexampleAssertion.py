import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

@pytest.mark.skip
def test_sampleA(setup_and_teardown):
    a=5
    b=6
    assert a==b, "a is not equal to b"
@pytest.mark.regression
def test_sampleB(setup_and_teardown):
    a=8
    b=4
    assert a>b, "this msg wont display"
@pytest.mark.smoke
def test_sampleC(setup_and_teardown):
    first_name="vinay"
    last_name="giri"
    assert first_name.__eq__(last_name), "first name is not equal to last name"

@pytest.mark.xfail
def testxfail(setup_and_teardown):
    print("failed")
    assert False

@pytest.mark.xfail
def testxpass(setup_and_teardown):
    print("something something")


#to run test function in the terminal use : pytest -k "not sampleA" -rA
#C:\Users\shambhu nath giri\PycharmProjects\FirstPythonProject\python\selenium\dr\justpackageforpytestchec> py.test test_smapling.py
# to change directory in terminal use : cd python//selenium//dr//justpackageforpytestchec
# to go back in directory or previous directory cd..
# pytest -rA --junit-xml="repot.xml"
# pytest -rA --html="reporting.html" install html if html report is not generated using pip install pytest-html
# pytest -rA -m smoke
# pytest -rA -m regression
# pytest -rA -m "smoke or regression"
# To change directory within python project use something like : cd python//selenium//dr