from python_training.selenium.page_object_swag_lab.pages.loginPage import login_page
from python_training.selenium.page_object_swag_lab.pages.productPage import product_Page
from python_training.selenium.page_object_swag_lab.tests.SelenuimBaseSwagLabs import seleniumBaseSwagLabs


class ProductPriceTest ():
    base = seleniumBaseSwagLabs()
    driver = base.selenium_init("https://www.saucedemo.com/")

    login_page_object = login_page(driver)
    product_page_object = product_Page(driver)

    login_page_object.login_to_swag_lab("standard_user","secret_sauce")
    product_page_object.get_first_price()



    base.selenium_end(driver)