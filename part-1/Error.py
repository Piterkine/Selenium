# 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()
time.sleep(3)

# Locate user name by id
# username = driver.find_element(By.Id, value='user-name')
# username = driver.find_element(By.NAME, value='user-name')
# password = driver.find_element(By.ID, value='password')
# Lbtn = driver.find_element(By.XPATH, value= '//input[@id = "login-button"]')
#~ addToCart = driver.find_element(By.XPATH, value = '//button[contains(@class, "btn_inventory")]')
#~ jacket = driver.find_element(By.XPATH, value= "//div[text() = 'Sauce Labs Fleece Jacket']")

# ! Finding element using multiple condition (AND & OR )
# Uname = driver.find_element(By.XPATH, value= "//input[@name = 'user-name' and @id = 'user-name']")
# Pass = driver.find_element(By.XPATH, value = "//input[@name = 'password' or @id = 'Pass']")

# ! Find by index in Xpath
# btn = driver.find_element(By.XPATH, value = "(//input)[3]")


# & Find element by link Text

# linkText = driver.find_element(By.LINK_TEXT, value = "Sauce Labs Backpack")
# linkText = driver.find_element(By.PARTIAL_LINK_TEXT, "Sauce Labs")



# username.send_keys('standard_user')
# password.send_keys('secret_sauce')
# Uname.send_keys('standard_user')
# Pass.send_keys('secret_sauce')

# Login btn click

# Lbtn.click( )
# btn.click( )
# time.sleep(2)


#~ addToCart.click()
#~ jacket.click()
# linkText = driver.find_element(By.PARTIAL_LINK_TEXT, "Sauce Labs")
# linkText.click()
# time.sleep(2)

time.sleep(3)
driver.quit()