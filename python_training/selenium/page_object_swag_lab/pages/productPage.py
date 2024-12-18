from selenium.webdriver.common.by import By


class product_Page ():
    def __init__(self,driver):
        self.driver = driver
        self.first_price_by_css = "div[class='inventory_item_price']"


    def get_first_price(self):
        print ("into get first price")

    def get_first_price_by_css(self,text):
        print ("into get first price")
        print (f"printing text {text}")
        first_price = self.driver.find_element(By.CSS_SELECTOR,self.first_price_by_css)
        price_as_text = first_price.text
        print (f"{price_as_text}")




    def get_all_prices(self):
        pass




