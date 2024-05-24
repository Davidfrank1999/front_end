# Work flow- outline
# 1) Open Web Browser(Chrome/firefox/IE). 
# 2) Open URL https://admin-demo.nopcommerce.com/login 
# 3) Provide Email (admin@yourstore.com). 
# 4) Provide password (admin). 
# 5) Click on Login. 
# 6) Capture title of the dashboad page.(Actual title) 
# 7) _ the page: "Dashboard / nopCommerce administration” (Expected) 
# 8) close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

serv_obj=Service(executable_path="Selenium\drivers\chromedriver-win64\chromedriver.exe")
# Here this accepts the driver path

#1) chrome browser
driver=webdriver.Chrome(service=serv_obj)

#2) Open URL
driver.get("https://admin-demo.nopcommerce.com/login")
time.sleep(5) # this is for my own observation


#3) username entry (Email)
Email_box=driver.find_element(By.NAME,"Email")
Email_box.clear()
Email_box.send_keys("admin@yourstore.com")

#4) password enter + click Enter
pass_box=driver.find_element(By.ID,"Password")
pass_box.clear()
pass_box.send_keys("admin")
#pass_box.send_keys("admin" + Keys.ENTER) #if want to press Enter key
time.sleep(4)


#5) Click on the login button
login_button=driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
login_button.click()

#6) Capture title of the dashboad page.
act_title=driver.title
exp_title="Dashboard / nopCommerce administration"
#7) compare
if act_title==exp_title:
	print("Login Test Passes")
else:
	print("Login Test Failed")
 
# 8) close browser
driver.quit()

#----