import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from python_training.selenium.SelenuimBase import seleniumBase

base = seleniumBase()
driver = base.selenium_init("https://www.saucedemo.com/")
base.login_to_swag_labs(driver)


drop_down = driver.find_element(By.CLASS_NAME, "product_sort_container")
drop_down_as_select = Select(drop_down)
drop_down_as_select.select_by_visible_text("Price (low to high)")




time.sleep(10)
base.selenium_end(driver)
