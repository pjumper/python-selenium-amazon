from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):

    SIGN_IN_EMAIL_FIELD = (By.CSS_SELECTOR, '#ap_email')
    def sign_in_email(self):
        self.find_element(*self.SIGN_IN_EMAIL_FIELD)
        assert self.find_element(*self.SIGN_IN_EMAIL_FIELD), f'Element is present'