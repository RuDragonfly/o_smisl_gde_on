from .base_page import BasePage
from .locators import ProductPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import time


class ProductPage(BasePage):
    
    def should_be_page_object(self):
        self.should_be_basket_click()
        self.should_be_product_name_eq_message()
        self.should_be_price_eq_cost_basket()

    def should_be_basket_click(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()
               
    def should_be_product_name_eq_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN)
        print(product_name.text)
        product_message = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE)
        print(product_message.text)
        assert product_message.text == product_name.text, 'The message is not equal to the product name'
        
    def should_be_price_eq_cost_basket(self): 
        #WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element(ProductPageLocators.PRICE))
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        print(price.text)
        cost_basket = self.browser.find_element(*ProductPageLocators.COST_BASKET)
        print(cost_basket.text)
        assert price.text == cost_basket.text, 'The price is not equal to the cost of the bascet'
    
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_MESSAGE), \
        "Success message is presented, but should not be"
      
    def should_disappeared_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_MESSAGE), \
        "Success message is not disappeared, but should be"
