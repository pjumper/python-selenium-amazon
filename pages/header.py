from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header (Page):

    CLICK_ORDER_BTTN = (By.CSS_SELECTOR, '#nav-orders')
    CLICK_CART_BTTN = (By.CSS_SELECTOR, '#nav-cart')
    def click_order_button(self):
        self.click(*self.CLICK_ORDER_BTTN)


    def click_cart_button(self):
        self.click(*self.CLICK_CART_BTTN)