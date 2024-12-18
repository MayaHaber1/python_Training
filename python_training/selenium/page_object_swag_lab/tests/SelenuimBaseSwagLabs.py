from selenium import webdriver
from selenium.webdriver.common.by import By


class seleniumBaseSwagLabs:

    def selenium_init(self, url):
        print ("test start")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        return driver

    def selenium_end(self,driver):
        driver.close()
        print ("test end")

    def login_to_swag_labs (self,driver):
        user_name = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login = driver.find_element(By.ID, "login-button")

        user_name.click()
        user_name.send_keys("standard_user")

        password.click()
        password.send_keys("secret_sauce")

        login.click()
