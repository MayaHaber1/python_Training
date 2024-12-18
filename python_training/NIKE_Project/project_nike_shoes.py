from selenium.webdriver.common.by import By
from python_training.selenium.SelenuimBase import seleniumBase
import time

base = seleniumBase()
driver = base.selenium_init("https://www.nike.com/il/")

def select_category_women(driver):
    women_category = driver.find_element(By.LINK_TEXT, "Women")
    women_category.click()
    time.sleep(2)

    best_seller = driver.find_element(By.LINK_TEXT, "Best Sellers")
    best_seller.click()
    time.sleep(2)

    shoes_category = driver.find_element(By.LINK_TEXT, "Shoes")
    shoes_category.click()
    time.sleep(2)

    women_shoe_name = driver.find_element(By.CSS_SELECTOR, "a.product-card__link-overlay").text
    print(f"Most popular shoes for women are {women_shoe_name}")

def select_category_men(driver):
    men_category = driver.find_element(By.LINK_TEXT, "Men")
    men_category.click()
    time.sleep(2)

    best_seller = driver.find_element(By.LINK_TEXT, "Best Sellers")
    best_seller.click()
    time.sleep(2)

    shoes_category = driver.find_element(By.LINK_TEXT, "Shoes")
    shoes_category.click()
    time.sleep(2)

    men_shoe_name = driver.find_element(By.CSS_SELECTOR, "a.product-card__link-overlay").text
    print(f"Most popular shoes for men are {men_shoe_name}")

if select_category_women != select_category_men:
        print(f"Men and women most popular shoes are not the same")
else:
        print(f"Same shoes for men and women")


select_category_women(driver)
select_category_men(driver)

base.selenium_end(driver)

