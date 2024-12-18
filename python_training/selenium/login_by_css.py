from selenium.webdriver.common.by import By
import time
from python_training.selenium.SelenuimBase import seleniumBase

base = seleniumBase()
driver = base.selenium_init("https://www.saucedemo.com/")

user = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
user.click()
user.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password.click()
password.send_keys("secret_sauce")






time.sleep(5)
base.selenium_end(driver)


