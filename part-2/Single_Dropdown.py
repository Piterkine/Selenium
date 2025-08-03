from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# ! Webdriver initialize
driver = webdriver.Chrome()
driver.maximize_window()

# ! Open the web elements page
driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

# ! locate the sigle select dropdown
dropDown =  Select(driver.find_element(By.ID, value= "carBrands"))


# ! Check dropdown is single Selector Or MultiSelector
if dropDown.is_multiple:
          print("This is multi selector")

else:
        print("This is single selector")



# ! Select option by visible text, value and index
dropDown.select_by_visible_text("Mercedes")
print("Selected option : ", dropDown.first_selected_option.text)


time.sleep(2        )

dropDown.select_by_value("audi")
print("Selected option : ", dropDown.first_selected_option.text)


time.sleep(2)

dropDown.select_by_index(1)
print("Selected option : ", dropDown.first_selected_option.text)


driver.quit()