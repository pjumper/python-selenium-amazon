from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):

    CART_PAGE_COUNT = (By.CSS_SELECTOR, '.nav-cart-count')
    NO_INSURANCE_BTTN = (By.ID, 'attachSiNoCoverage')


    def click_no_insurance_bttn(self):
        self.click(*self.NO_INSURANCE_BTTN)



    def verify_cart_empty(self, expected_count):
        actual_count = self.find_element(*self.CART_PAGE_COUNT).text
        assert expected_count == actual_count, f'expected{expected_count} but got {actual_count}'

    def verify_cart_count(self, expected_count):
        actual_count = self.find_element(*self.CART_PAGE_COUNT).text
        assert expected_count == actual_count, f'Expected this amount {expected_count} but received this amount {actual_count}'
