from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

serv_obj = Service(executable_path="Selenium\\drivers\\chromedriver-win64\\chromedriver.exe")

@given('I launch chrom_browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=serv_obj)

@when('I open OrangeHRM home_page')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

@when('Enter username "{username}" and password "{password}"')
def enter_credentials(context,username,password):
    context.driver.find_element(By.NAME, "username").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)


@when('Click on login button')
def click_login_button(context):
    context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(5)
    
@then('User must successfully login to the dashboard_page')
def verify_login(context):
    try:
        text = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
    except:
        context.driver.close()
        assert False,"Test Failed"
    if text=="dashboard":
        context.driver.close()
        assert True,"Test Passed"
