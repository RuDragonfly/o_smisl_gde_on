from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, 'login is not presented in url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login-Username is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login-Password is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATONS_EMAIL), "Registration-email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATONS_PASSWORD1), "Registration-password1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATONS_PASSWORD2), "Registration-password2 is not presented"
        
    def register_new_user(self):#,email,password):
        
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())+'v56fglhkjvgjgh'
               
        registrations_email = self.browser.find_element(*LoginPageLocators.REGISTRATONS_EMAIL)
        registrations_email.send_keys(email)
        
        registrations_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATONS_PASSWORD1)
        registrations_password1.send_keys(password)
        
        registrations_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATONS_PASSWORD2)
        registrations_password2.send_keys(password)
                      
        btn_register = self.browser.find_element(*LoginPageLocators.BTN_REGISTER)
        btn_register.click()
        
        
        
