import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get ("https://www.saucedemo.com/")

user_name = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")

user_name.click()
user_name.send_keys("standard_user")

password.click()
password.send_keys("secret_sauce")

login.click()




time.sleep(3)
driver.close()