from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):


    def open_main(self):
        self.open_url('https://www.amazon.com/')