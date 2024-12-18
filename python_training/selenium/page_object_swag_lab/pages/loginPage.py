from selenium.webdriver.common.by import By

from python_training.my_first_test import user_name
from python_training.selenium.SwagLabs import driver


class login_page():

    def __init__(self,driver):
        self.driver = driver
        self.user_name_locator = "user-name"
        self.password_locator = "password"
        self.login_locator = "login-button"

    def login_by_css(self):
        user_name = self.driver.find_element(By.CSS_SELECTOR)





    def login_to_swag_lab (self,user_name_text,password_text):
        print ("into login to swag labs")
        user_name = self.driver.find_element(By.ID, self.user_name_locator)
        password = self.driver.find_element(By.ID, self.password_locator)
        login_button = self.driver.find_element(By.ID, self.login_locator)
        user_name.click()
        user_name.send_keys(user_name_text)

        password.click()
        password.send_keys(password_text)

        login_button.click()




        pass
