from selenium import webdriver
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.locators import BasePageLocators
import time
import pytest

class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user()
        self.page = BasePage(browser, link)
        self.page.should_be_authorized_user()
   
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link) 
        page.open()  
        page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        # нажимаем кнопку корзины
        page = ProductPage(browser, link) 
        page.open()  
        page.should_be_basket_click() 
        page.should_be_product_name_eq_message()
        page.should_be_price_eq_cost_basket()
 
@pytest.mark.need_review   
@pytest.mark.parametrize('link', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    # нажимаем кнопку корзины
    page = ProductPage(browser, link) 
    page.open()  
    page.should_be_basket_click() 
    # считаем по формуле и вписываем ответ
    page.solve_quiz_and_get_code()
    # Проверки ожидания
    time.sleep(7)
    page.should_be_product_name_eq_message()
    page.should_be_price_eq_cost_basket()
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()  
    page.should_be_basket_click() 
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()  
    page.should_not_be_success_message()
    
@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()  
    page.should_be_basket_click() 
    page.should_disappeared_success_message()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
    
@pytest.mark.need_review         
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasePage(browser, link)
    page.open()
    #открываем корзину из base_page
    page.view_basket()
    #переходим на страницу корзины
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_basket_is_empty()
    
     
