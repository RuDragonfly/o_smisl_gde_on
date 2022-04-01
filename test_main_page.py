from pages.main_page import MainPage

#link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор драйвер и url адрес 
    page = MainPage(browser, link) 
    # открываем страницу
    page.open()  
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page() 
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

#def go_to_login_page(browser):
    link = browser.find_element_by_css_selector("#login_link")
    link.click()
#
#def test_guest_can_go_to_login_page(browser): 
#    browser.get(link) 
#    go_to_login_page(browser) 
