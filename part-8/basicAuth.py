import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# ✅ Step 1: Create Chrome options
options = Options()

# ✅ Step 2: Use the new profile directory
options.add_argument("--user-data-dir=C:\\Temp\\SeleniumProfile")  # Path to the new folder

# ! Disable the chrome setting option

# ✅ Step 3: Clean browsing experience (disable popups, notifications)
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--log-level=3")  # Suppress unnecessary logs


# ! Intitalize chrome browser and launch browser
driver = webdriver.Chrome(options=options)

print('Browser Opened')

# ! Maimize the window size
driver.maximize_window()
print("Browser Maximize")

# ! Open url
 
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

#capture response of basic authentication

message = driver.find_element(By.TAG_NAME,"p")

print("Response:", message.text)

#wait for 5 sec
time.sleep(5)

#close broswer
driver.quit()
print("Browser closed")
