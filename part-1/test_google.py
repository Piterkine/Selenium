from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the Chrome browser
driver = webdriver.Chrome()

# Go to Google
driver.get("https://www.google.com")

# Find the search input box by name and type a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()

# Wait for results to load
time.sleep(15)

# Close the browser
driver.quit()
