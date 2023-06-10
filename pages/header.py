from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header (Page):

    CLICK_ORDER_BTTN = (By.CSS_SELECTOR, '#nav-orders')
    CLICK_CART_BTTN = (By.CSS_SELECTOR, '#nav-cart')
    CLICK_BESTSELLERS_TAB = (By.CSS_SELECTOR, 'a[href*=nav_cs_bestsellers')
    BESTSELLERS_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    CLICK_SEARCH_BTTN = (By.ID, 'nav-search-submit-button')
    def click_order_button(self):
        self.click(*self.CLICK_ORDER_BTTN)


    def click_cart_button(self):
        self.click(*self.CLICK_CART_BTTN)



    def click_bestsellers_tab(self):
        self.click(*self.CLICK_BESTSELLERS_TAB)

    def click_search_button(self):
        self.click(*self.CLICK_SEARCH_BTTN)

    def input_text_search_field(self, text):
        self.input_text(text,*self.SEARCH_FIELD)


    def verify_bestseller_links_displayed(self, expected_links):
        bestseller_links = self.find_elements(*self.BESTSELLERS_LINKS)
        expected_links = int(expected_links)
        assert len(bestseller_links) == expected_links, f'Expected {expected_links} but got {bestseller_links}'



