import time

from selenium.webdriver.common.by import By
from python_training.selenium.SelenuimBase import seleniumBase

base = seleniumBase()
driver = base.selenium_init("https://demo.guru99.com/test/newtours/reservation.php/")

buttons = driver.find_element(By.NAME,"tripType")
buttons[1].click()
buttons[0].click()


time.sleep(5)
base.selenium_end(driver)

