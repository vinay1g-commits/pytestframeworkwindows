import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# To remove automation message from chrome
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.careerindia.com/entrance-exam/gate-exam-e19.html")
time.sleep(3)
table = driver.find_element(By.XPATH,"//table[2]")
table.location_once_scrolled_into_view

# To retrieve table heading
table_head = driver.find_elements(By.XPATH,"//table[2]/tbody/tr[1]//td")
for list in table_head:
    print(list.text)

# To retrieve entire table data
table_data = driver.find_elements(By.XPATH,"//table[2]//td")
for list2 in table_data:
    print(list2.text)

# To retrieve only the second row of table
first_row = driver.find_elements(By.XPATH,"//table[2]//tr[2]")
for list3 in first_row:
    print("=============================")
    print(list3.text)

# To retrieve third column data in 3rd row that is 3rd cell
third_cell = driver.find_element(By.XPATH,"//table[2]//tr[4]//td[3]")
print("cell value is :")
print(third_cell.text)

# To Retrieve all data of third column
third_colmn = driver.find_elements(By.XPATH,"//table[2]//tr//td[3]")
for list4 in third_colmn:
    print("third column data is:")
    print(list4.text)

# To find number of rows or columns in a table
rows_num = driver.find_elements(By.XPATH,"//table[2]//tr")
print("num of rows are:")
print(len(rows_num))

colmn_num = driver.find_elements(By.XPATH,"//table[2]//td")
print("num of colmns are:") #untill <th> tag is present in the table you can't find number of columns
print(len(colmn_num))
time.sleep(2)
