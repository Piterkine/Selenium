from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

# ! Select radio button
rBtn1 = driver.find_element(By.ID, value = "radio1")
rBtn2 = driver.find_element(By.ID, value = "radio2")

# ! Button click
rBtn1.click()
print("Ford selected : ", rBtn1.is_selected()) #& Return true/False

rBtn2.click()
print("bwm selected : ", rBtn2.is_selected())   #& Return true/False
print("Ford selected : ", rBtn1.is_selected())  #& Return true/False
time.sleep(2)

driver.quit()
