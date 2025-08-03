from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.saucedemo.com/v1/')

time.sleep(1)

#! Find all input fields(username and password) using find_elements()

# input_fields = driver.find_elements(By.TAG_NAME, value = "input")
input_fields = driver.find_elements(By.XPATH, value = "//input")


# print(type(input_fields))
# print(len(input_fields))

#! find index of username and password with manual.

# print(input_fields[0].get_attribute('id'))
# print(input_fields[1].get_attribute('id'))
# print(input_fields[2].get_attribute('id'))

#! find index of username and password with loop.

# index = 0
# for field in input_fields:
#           print(f"index is {index}: {field.get_attribute('id')}")
#           index = index + 1

input_fields[0].send_keys('standard_user')
input_fields[1].send_keys('secret_sauce')
input_fields[2].click()
 
# ! List all the product  using find_elements

product = driver.find_elements(By.XPATH, value = "//div[@class = 'inventory_item_name']")

index = 0
for item in product:
          print(f"index {index} : {item.text}")
          index = index + 1

time.sleep(2)

driver.quit()

# userName = driver.find_element(By.ID, value="user-name")

# userName.send_keys("standard_key")