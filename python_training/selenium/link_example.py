import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from python_training.selenium.SelenuimBase import seleniumBase

base = seleniumBase()
driver = base.selenium_init("https://demo.guru99.com/test/newtours/index.php")


hotels_button = driver.find_element(By.LINK_TEXT,"Hotels")
hotels_button.click()

vacation_button = driver.find_element(By.PARTIAL_LINK_TEXT,"Vacations")
vacation_button.click()



base.selenium_end(driver)
print ("test end")
time.sleep(10)
driver.close()