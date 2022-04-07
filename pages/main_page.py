from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    
    def should_be_basket_click(self):
        btn = self.browser.find_element(*MainPageLocators.BTN_ADD_TO_BASKET)
        btn.click()  
    
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEMS), \
        "Basket_items is presented, but should not be"

    def should_be_basket_is_empty(self):
        basket_message = self.browser.find_element(*MainPageLocators.BASKET_IS_IMPTY) 
        assert basket_message.text == 'Your basket is empty.', 'Your basket is not empty.'
   
