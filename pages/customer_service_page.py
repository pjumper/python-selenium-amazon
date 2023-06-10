from selenium.webdriver.common.by import By
from pages.base_page import Page

class CustomerServicePage(Page):

    WELCOME_TEXT = (By.CSS_SELECTOR, 'h1.fs-heading.bolded')
    CUST_SERV_UI_LINKS = (By.CSS_SELECTOR, '.issue-card-container .issue-card-wrapper')
    SEARCH_LIBRARY_TEXT = (By.XPATH, "//h2[text()='Search our help library']")
    HELP_LIBR_SEARCH_FIELD = (By.ID, 'hubHelpSearchInput')
    ALL_HELP_TOPICS_TEXT = (By.XPATH, "//h2[text()='All help topics']")
    RECOMMEND_TOPIC_LINKS = (By.CSS_SELECTOR, 'ul.help-topics li')
    def open_cust_service_page(self):
        self.open_url('https://www.amazon.com/hz/contact-us/foresight/hubgateway')


    def verify_welcome_text(self):
        assert self.find_element(*self.WELCOME_TEXT).is_displayed()


    def verify_cust_serv_links(self, expected_links):
        actual_links = self.find_elements(*self.CUST_SERV_UI_LINKS)
        expected_links = int(expected_links)
        assert len(actual_links) == expected_links, f'Expected {expected_links} links but got {actual_links} links'

    def verify_search_library_text_present(self, expected_text):
        actual_text = self.find_element(*self.SEARCH_LIBRARY_TEXT).text
        assert expected_text == actual_text, f'Expected text {expected_text} but got {actual_text}'


    def verify_help_library_search_field(self):
        assert self.find_element(*self.HELP_LIBR_SEARCH_FIELD).is_displayed()


    def verify_help_topics_text_present(self, expected_text):
        actual_text = self.find_element(*self.ALL_HELP_TOPICS_TEXT).text
        assert expected_text == actual_text, f'Expected text {expected_text} but got {actual_text} text'


    def verify_recommend_topic_links_present(self, expected_links):
        expected_links = int(expected_links)
        actual_links = self.find_elements(*self.RECOMMEND_TOPIC_LINKS)
        assert len(actual_links) == expected_links, f'Expected {expected_links} but got {actual_links}'