
#& Explicit Wait: Applies a wait time for a particular element(Condition) not all element..
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  #^ ✅ Required for using Keys like Keys.RETURN
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
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

# ! Open url

driver.get("https://duckduckgo.com/")
print("Url opened")
wait = WebDriverWait(driver, 10,)                # & Use explicit wait to locate the search box
searchBox = wait.until(Ec.presence_of_element_located((By.NAME, "q")))

# !send input in search box
searchBox.send_keys("What do QA engineer in software Company")


# !Press enter key to submit the seacrh string

searchBox.send_keys(Keys.RETURN)
time.sleep(3)

# !Close browser
driver.quit()
print("Browser Closed")


