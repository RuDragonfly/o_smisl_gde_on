from selenium import webdriver
from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.product_page import ProductPage
import time
import pytest

@pytest.mark.skip 
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор драйвер и url адрес 
    page = MainPage(browser, link) 
    # открываем страницу
    page.open()  
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page() 
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
@pytest.mark.skip    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.skip 
def test_guest_should_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    
@pytest.mark.skip    
def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
@pytest.mark.skip   
def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
@pytest.mark.skip 
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # нажимаем кнопку корзины
    page = ProductPage(browser, link) 
    page.open()  
    page.should_be_basket_click() 
    # считаем по формуле и вписываем ответ
    page.solve_quiz_and_get_code()
    # Проверки ожидания
    time.sleep(5)
    page.should_be_product_name_eq_message()
    page.should_be_price_eq_cost_basket()
    
@pytest.mark.skip 
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
    
@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()  
    page.should_be_basket_click() 
    page.should_not_be_success_message()
    
@pytest.mark.skip    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()  
    page.should_not_be_success_message()
    
@pytest.mark.skip     
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
    #time.sleep(5)
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
    
