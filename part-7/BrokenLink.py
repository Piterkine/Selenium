import time
import requests
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

# driver.get("https://practice.expandtesting.com/") #& 1st link
driver.get("http://www.deadlinkcity.com/")  #& 2nd link
print("Url opened")
time.sleep(3)

# ! Find all link on website
# alink = driver.find_elements(By.TAG_NAME, value= "a")
alink = driver.find_elements(By.XPATH, value= "//a")
print(f"Total link found {len(alink)}")

brkoen = 0
valid = 0
for link in alink:
          url = link.get_attribute("href")

# ^ We know some fake link present in our website so they are easily crash/ stop our script. With the help of try and exepect we easily skip fail link and script run properly

          try: 
                  response = requests.head( url, timeout= 5)  #* Timeout is maximum time wait for response
                  if response.status_code >= 400:
                               print("Broken link: ", link.text)
                               brkoen += 1

                  else:
                              print("Valid link..", link.text)
                              valid += 1

          except Exception as e:                   #& You can skip the error by using except: None
                  print(f"Error happened", e)
                  
                  
          
         


print("No of link valid: ", valid)
print("No of Broken link: ", brkoen)
time.sleep(2)

# ! Close Browser
driver.quit()
print("Browser Closed")

