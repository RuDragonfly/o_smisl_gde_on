from selenium.webdriver.common.by import By

class MainPageLocators():
    
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_IMPTY = (By.CSS_SELECTOR,'#content_inner > p')
    
class LoginPageLocators:
    REGISTRATONS_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATONS_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATONS_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BTN_REGISTER = (By.CSS_SELECTOR, '#register_form > button') 
    
class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_MAIN = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    COST_BASKET = (By.CSS_SELECTOR,'.alert-info .alertinner strong')
    PRICE = (By.CSS_SELECTOR,'.col-sm-6>.price_color')
    BTN_INFO = (By.CSS_SELECTOR,'#messages > div:nth-child(3) .alertinner .btn-info')
    
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
   
