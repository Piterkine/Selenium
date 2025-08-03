from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Launch Chrome
driver = webdriver.Chrome()  # or use Chrome(executable_path="path/to/chromedriver")

# Step 2: Open Google
driver.get("https://www.google.com")

# Optional: Maximize window
driver.maximize_window()

# Step 3: Find the search input box
search_box = driver.find_element(By.NAME, "q")

# Step 4: Enter a search query
search_box.send_keys("Selenium with Python")

# Step 5: Press Enter
search_box.send_keys(Keys.RETURN)

# Optional: Wait a few seconds to see results
time.sleep(5)

# Step 6: Close browser
driver.quit()
