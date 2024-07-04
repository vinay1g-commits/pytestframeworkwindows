import self
from appium import webdriver
import unittest
#from typing import Any, Dict
#from appium.options.common import AppiumOptions
#from appium.webdriver.common.appiumby import AppiumBy

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='11'
desired_caps['deviceName']='samsung SM-A507FN'
desired_caps['app']='D:\\apk files\\firefox-124-2-0.apk'
self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



"""url = "http://127.0.0.1:5037/"
# driver = dr.Remote("http://localhost:4723/wd/hub", desired_cap)
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Firefox")
element.click()
driver.quit()
"""