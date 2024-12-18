import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get ("https://www.google.com/")
search = driver.find_element(By.NAME,"q")

search.click()
search.send_keys("cat")
search.send_keys(Keys.ENTER)

time.sleep(10)
driver.close()

