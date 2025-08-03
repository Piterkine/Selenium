from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# ! Open url in web browser.

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(3)

# ! Find custom dropdown web element.

dropdown = driver.find_element(By.ID, value = "custom-select" )

# ! Use javaScript to scroll the page to make dropdown visible

driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(3)

dropdown.click()  #& Open DropDown to perform Click action


# ! find option Red in dropdown

optRed = driver.find_element(By.XPATH, value = "//div[@class = 'custom-options']/div[text() = 'Red']")

optRed.click()
time.sleep(2)


# ! Find blue option 
dropdown.click()  #& Open DropDown to perform Click action
optBlue = driver.find_element(By.XPATH, value="//div[@class = 'custom-options']/div[text() = 'Blue']")
optBlue.click()
time.sleep(2)


driver.quit()