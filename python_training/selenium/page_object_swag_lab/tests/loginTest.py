import time

from python_training.selenium.page_object_swag_lab.pages.loginPage import login_page
from python_training.selenium.page_object_swag_lab.tests.SelenuimBaseSwagLabs import seleniumBaseSwagLabs


class Login_test():
    base = seleniumBaseSwagLabs()
    driver = base.selenium_init("https://www.saucedemo.com/")

    login_page_object = login_page(driver)

    login_page_object.login_to_swag_lab("standard_user", "secret_sauce")


    time.sleep(5)
    base.selenium_end(driver)
