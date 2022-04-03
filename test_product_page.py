from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.product_page import PageObject
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # нажимаем кнопку корзины
    page = PageObject(browser, link) 
    page.open()  
    page.should_be_basket_click() 
    # считаем по формуле и вписываем ответ
    page.solve_quiz_and_get_code()
    # Проверки ожидания
    time.sleep(5)
    page.should_be_product_name_eq_message()
    page.should_be_price_eq_cost_basket()
    
    
    
    
    
