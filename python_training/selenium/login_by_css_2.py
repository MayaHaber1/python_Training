from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from python_training.selenium.SelenuimBase import seleniumBase
import time


base = seleniumBase()
driver = base.selenium_init("https://demo.applitools.com/app.html")



search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Start typing to search...']")
search_box.click()
search_box.send_keys("HELLO")



time.sleep(5)

base.selenium_end(driver)