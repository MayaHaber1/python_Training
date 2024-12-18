import time
from selenium.webdriver.common.by import By


from python_training.selenium.SelenuimBase import seleniumBase

base = seleniumBase()
driver = base.selenium_init("https://www.saucedemo.com/")
user_name = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")

user_name.click()
user_name.send_keys("standard_user")

password.click()
password.send_keys("secret_sauce")

login.click()

first_price = driver.find_element(By.CLASS_NAME, "inventory_item_price")
first_price_text = first_price.text

prices = driver.find_element(By.CLASS_NAME,"inventory_item_price")
second_price_element = prices[1]
second_price_text = second_price_element.text

second_displayed = second_price_element.is_displayed()






time.sleep(10)
base.selenium_end(driver)