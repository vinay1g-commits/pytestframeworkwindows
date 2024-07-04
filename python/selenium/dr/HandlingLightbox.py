import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
time.sleep(5)
view=driver.find_element(By.XPATH,"(//div[@class='oi-slider oi-youtube margin-bottom'])[1]")
print(view.rect)


#video=driver.find_element(By.XPATH,"(//div[@class='oi-heading-2'])[1]")
#video.location_once_scrolled_into_view
#time.sleep(10)
driver.execute_script("window.scrollTo(451.5,2420)")
time.sleep(5)
driver.execute_script("window.scrollTo(0,250)")
slide=driver.find_element(By.XPATH,"(//div[@class='oi-slider-text'])[1]")
time.sleep(2)
slide.click()

