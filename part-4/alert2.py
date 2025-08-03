from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/alerts")

# ! Find button element
# Abtn = driver.find_element(By.ID, value = "alertButton")
# Cbtn = driver.find_element(By.ID, value = "confirmButton")
Pbtn = driver.find_element(By.ID, value = "promptButton")


# ! Click on button

# Abtn.click()
# Cbtn.click()
Pbtn.click()
time.sleep(2)

# ! Switch focus to alert pop-up

# alert = driver.switch_to.alert
# print("Simple Alert Message :", alert.text)
# time.sleep(2)

# Confirm = driver.switch_to.alert
# print("Confirm message : ", Confirm.text)
# time.sleep(2)

Prompt = driver.switch_to.alert
print("Prompt message: ", Prompt.text)
time.sleep(2)

# ! Click on alert Ok button by accepting alert
# alert.accept()

# ! Click on Confirm Ok, Cancel button by accepting alert
# Confirm.accept()
# Confirm.dismiss()
# time.sleep(1)

# simple_alert = driver.switch_to.alert
# print("Inside Confirm pop_up: ",simple_alert.text)
# time.sleep(5)
# simple_alert.accept()

# ! Click on prompt button by accepting alert.

# & Enter text in prompt alert
Prompt.send_keys("Jai ho ")   
Prompt.accept()
time.sleep(5)

second_alert =driver.switch_to.alert
print('Second Alert: ', second_alert.text )
time.sleep(3)
second_alert.accept()
 
# ! Cloase browser
driver.quit()