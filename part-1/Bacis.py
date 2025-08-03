# Import webDriver module from selenium package
from selenium import webdriver
# from selenium.webdriver.common.by import By
import time

# Initantiate webDriver and launch Chrome
Driver = webdriver.Chrome()

# Open url Google
Driver.get('https://google.com/')
time.sleep(3)

# Open url youtube
Driver.get('https://youtube.com/')
time.sleep(2)

# Go back
Driver.back()
time.sleep(2)

#  go forward to youtube
Driver.forward()
time.sleep(2)

# refresh the current page
Driver.refresh()
time.sleep(2)

# Time for open upto


# Close browser
Driver.quit() 