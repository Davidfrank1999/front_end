from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

serv_obj=Service(executable_path="Selenium\drivers\chromedriver-win64\chromedriver.exe")


@given('launch chrom_browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(service=serv_obj)
    


@when('open OrangeHRM home_page')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

@then('verify that the Logo presence on home_page')
def verifylogo(context):
    logo=context.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[1]/img")
    assert logo.is_displayed() is True
    


@then('close chrom_browser')
def closeBrowser(context):
    context.driver.close()