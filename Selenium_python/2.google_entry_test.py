# Using Selenium to manipulate google
# Outline
#    1. open web Browser(Chrome)
#    2. Open URL https://www.google.com/
#    3. enter Text in search box and press Enter key

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

serv_obj=Service(executable_path="Selenium\drivers\chromedriver-win64\chromedriver.exe")

# 1 open chrome
driver=webdriver.Chrome(service=serv_obj)
time.sleep(5) # for observing the actions

# 2 open google
driver.get("https://www.google.com/")

# 3 type in search bar + enter to search
input_element=driver.find_element(By.ID,"APjFqb")
input_element.send_keys("Selenium python tutorial" + Keys.ENTER)
time.sleep(3)

# close
driver.quit()

#---