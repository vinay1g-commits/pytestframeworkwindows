import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.oneindia.com/")
time.sleep(3)
goldRates=driver.find_element(By.XPATH,"//select[@id='gold_rates']")
goldRates.location_once_scrolled_into_view
somethinglist=Select(goldRates)
if somethinglist.is_multiple:
    print("true its having multiple values which can be selected simultaneously")
else:
    print("false it cannot select contain multiple values at once")

storing=somethinglist.options
for s in storing:
    print(s.text)
time.sleep(2)
somethinglist.select_by_visible_text("Bangalore")
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
somethinglist.select_by_index(3)
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
somethinglist.select_by_value("https://www.goodreturns.in/gold-rates/mysore.html")
print(somethinglist.first_selected_option.text)
print("done")
time.sleep(2)
driver.quit()
#states=driver.find_element(By.XPATH,"(//span[@class='oi-level-selstate'])[1]")
#states.click()
