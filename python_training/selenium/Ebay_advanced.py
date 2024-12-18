import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from unicodedata import category

from python_training.selenium.SelenuimBase import seleniumBase

base = seleniumBase()
driver = base.selenium_init("https://www.ebay.com/")

advanced = driver.find_element(By.LINK_TEXT,"Advanced")
advanced.click()
time.sleep(3)

category = driver.find_element(By.ID , "s0-1-17-4[0]-7[3]-_sacat")
category_as_select = Select(category)
category_as_select.select_by_visible_text("Baby")



time.sleep(10)
base.selenium_end(driver)


