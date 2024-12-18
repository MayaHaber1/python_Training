from python_training.selenium.page_object_swag_lab.pages.loginPage import login_page
from python_training.selenium.page_object_swag_lab.pages.productPage import product_Page
from python_training.selenium.page_object_swag_lab.tests.SelenuimBaseSwagLabs import seleniumBaseSwagLabs
import time

class getFirstPrice:
    base = seleniumBaseSwagLabs()
    driver = base.selenium_init("https://www.saucedemo.com/")

    login_page_object = login_page(driver)
    product_page_object = product_Page(driver)
    login_page_object.login_to_swag_lab("standard_user", "secret_sauce")

    product_page_object.get_first_price_by_css("hello everyone")


    time.sleep(3)
    base.selenium_end(driver)

