from selenium import webdriver 
from selenium.webdriver.common.by import By #& to locate element on webpage
import time

driver = webdriver.Chrome()
driver.maximize_window()

# ! Open a link on window
driver.get("https://demo.guru99.com/V4/index.php")
time.sleep(1)

# ! Find login button
Lbtn = driver.find_element(By.NAME, value = "btnLogin")


# ! Click Login button 
Lbtn.click()
time.sleep(1)

# ! Handel alert method
alert = driver.switch_to.alert #& Switch focus to alert popup
alert.accept()


time.sleep(2) 


# ! Close browser     
driver.quit()

