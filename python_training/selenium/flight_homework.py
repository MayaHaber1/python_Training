
import time

from select import select
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from python_training.selenium.SelenuimBase import seleniumBase

base = seleniumBase()
driver = base.selenium_init("https://demo.guru99.com/test/newtours/reservation.php/")
time.sleep(3)
trip_type = driver.find_element(By.NAME, "tripType")
one_way = trip_type[1]
one_way.click()
on_menu = driver.find_element(By.NAME,"fromMonth")
on_as_drop_down = select(on_menu)
on_as_drop_down.select_by_index(3)
on_as_drop_down.select_by_visible_text("may")



time.sleep(10)
base.selenium_end(driver)