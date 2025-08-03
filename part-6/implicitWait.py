
# & Implicit wait : Applies a default wait time for all elements. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  #^ ✅ Required for using Keys like Keys.RETURN
import time

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
# driver = webdriver.Chrome()
print('Browser Opened')

# ! Maimize the window size
driver.maximize_window()
print("Browser Maximize")

# ! Add wait for 7 sec to all element
driver.implicitly_wait(7)


# ! Open url
driver.get("https://duckduckgo.com/")
print("Url opened")


# ! Find element by name 
searchBox = driver.find_element(By.NAME, value ="q")


# !send input in search box 
searchBox.send_keys("What do QA engineer in software Coampany")


# !Press enter key to submit the seacrh string

searchBox.send_keys(Keys.RETURN)
time.sleep(3)

# !Close browser
driver.quit()
print("Browser Closed")