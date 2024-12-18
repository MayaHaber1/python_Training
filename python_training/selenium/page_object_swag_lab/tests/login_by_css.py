from python_training.selenium.page_object_swag_lab.tests.SelenuimBaseSwagLabs import seleniumBaseSwagLabs

base = seleniumBaseSwagLabs()
driver = base.selenium_init("https://www.saucedemo.com/")
base.login_to_swag_labs(driver)

base.selenium_end(driver)

