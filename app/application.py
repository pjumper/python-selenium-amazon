from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage
from pages.customer_service_page import CustomerServicePage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.header = Header(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.customer_service_page = CustomerServicePage(self.driver)
