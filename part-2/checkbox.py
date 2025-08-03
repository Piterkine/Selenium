from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# driver.get('')
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

# ! fetch window title and print.
print('Title is: ', driver.title)

# ! fetch URL and print.
print ( 'URL : ', driver.current_url)

# ! find checkBox
# elem1 = driver.find_element(By.ID, value= 'option1')
# if not elem1.is_selected():              # yaha per agar ford vali value by default check hogi to usko uncheck nhi kerega .. 
#                     elem1.click() 

# time.sleep(2)

# elem2 = driver.find_element(By.ID, value = 'option2')
# elem2.click()
# time.sleep(1)

# ! Verify selected or diselected /

# print("Frod selected : ",elem1.is_selected())
# print("BMW selected : ",elem2.is_selected())


# ! Select multiple checkBox using find_elements and click 
checkBox = driver.find_elements(By.XPATH, value = "//input[@type = 'checkbox']")
for box in checkBox:
          if not box.is_selected():
                  box.click()
time.sleep(3)
driver.quit()

