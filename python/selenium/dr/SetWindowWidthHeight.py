import time
import os
from selenium import webdriver
user_agent="Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36"
profile=webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',user_agent)
path=os.path.join(os.getcwd(),'Drivers','geckodriver.exe')
driver=webdriver.Firefox(executable_path=path,firefox_profile=profile)
driver.maximize_window()
driver.get("https://www.oneindia.com/")
driver.set_window_size(300,800)
time.sleep(3)
driver.quit()