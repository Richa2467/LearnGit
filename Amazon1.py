import time


from selenium.webdriver.support import expected_conditions as EC

# import webdriver
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Locators
from Locators import *


driver = webdriver.Chrome()
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception])
driver.get(Url)
time.sleep(2)
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,account_link).click()






# 1.....invalid Phone Number
email_field = mywait.until(EC.presence_of_element_located((By.ID, email)))
email_field.send_keys("43722929")
time.sleep(2)
continue_button = mywait.until(EC.presence_of_element_located((By.ID, continue_butt)))
continue_button.click()
time.sleep(2)
# Error message
error_message = mywait.until(EC.presence_of_element_located((By.CLASS_NAME,error_message1)))
if "Incorrect phone number" in error_message.text:
    print("First Negative login test pass")
else:

    print("First Negative test case failed")
 # 2...blank phone number
email_field = mywait.until(EC.presence_of_element_located((By.ID,email)))
email_field.clear()
email_field.send_keys("698793")
time.sleep(8)
continue_button = mywait.until(EC.presence_of_element_located((By.ID,continue_butt)))
continue_button.click()
time.sleep(2)
error_message = mywait.until(EC.presence_of_element_located((By.XPATH, error_message2)))
if "Enter your email or mobile phone number" in error_message.text:
    print("Second Negative login test pass")
else:
    print("Second Negative test case failed")







# Verification

email_field = mywait.until(EC.presence_of_element_located((By.ID,email)))
email_field.clear()
email_field.send_keys("8200430861")
continue_button = mywait.until(EC.presence_of_element_located((By.ID,continue_butt)))
continue_button.click()
time.sleep(2)
password_field = mywait.until(EC.presence_of_element_located((By.ID,password)))
password_field.send_keys("Harshvi@1462")
signin_button = mywait.until(EC.presence_of_element_located((By.ID,submit_button)))
signin_button.click()
time.sleep(2)



if (mywait.until(EC.presence_of_element_located((By.ID, account_list))).text) == "Hello, Harshvi":
    print("User-verified")
else:
    print("User-not verified")



driver.close()