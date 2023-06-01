from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):

    ALL_COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    COLORS = (By.CSS_SELECTOR, 'span.selection')

    def open_product_b0bbjrr25(self):
        self.open_url('https://www.amazon.com/gp/product/B07BJKRR25/')


    def verify_user_can_click_thru_colors(self, *locator):
        self.find_elements(*self.ALL_COLOR_OPTIONS)
        expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage']
        all_color_options = self.find_elements(*self.ALL_COLOR_OPTIONS)

        actual_colors = []
        for color in all_color_options[:4]:
            color.click()
            current_color = self.find_element(*self.COLORS).text
            actual_colors += [current_color]
        assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'
