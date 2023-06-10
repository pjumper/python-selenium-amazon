from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):

    HAM_MENU = (By.ID, "nav-hamburger-menu")
    FOOTER_LINKS = (By.CSS_SELECTOR, ".navFooterLine a")
    HEADER_LINKS = (By.CSS_SELECTOR, '#nav-xshop-container .nav-a')

    def open_main(self):
        self.open_url('https://www.amazon.com/')

    def verify_ham_menu_present(self):
        assert self.find_element(*self.HAM_MENU).is_displayed(), f'Hamburger Menu is not present'
        # element_shown = self.find_element(*self.HAM_MENU)
        # print(element_shown)


    def verify_footer_link_count(self, expected_count):
        expected_count = int(expected_count)
        footer_links = self.find_elements(*self.FOOTER_LINKS)
        assert len(footer_links) == expected_count, f'Expected {expected_count} but got {footer_links}'

    def verify_header_link_count(self, expected_count):
        expected_count = int(expected_count)
        header_links = self.find_elements(*self.HEADER_LINKS)
        assert len(header_links) == expected_count, f'Expected {expected_count} but got {header_links}'