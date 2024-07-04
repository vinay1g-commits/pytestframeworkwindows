from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdr


cap:Dict[str,Any] = {"platformName": "Android",
               "automationName": "UiAutomator2",
               "deviceName": "samsung SM-A507FN"
               }
url = "http://localhost:5037/"
# driver = dr.Remote("http://localhost:4723/wd/hub", desired_cap)
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Firefox")
element.click()
driver.quit()