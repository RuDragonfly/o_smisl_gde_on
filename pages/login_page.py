from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

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
        
