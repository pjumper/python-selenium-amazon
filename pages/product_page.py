from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):

    ALL_COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    COLORS = (By.CSS_SELECTOR, 'span.selection')
    All_PRODUCTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
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


    def verify_product_name_image(self):
        self.find_elements(*self.All_PRODUCTS)
        all_products = self.find_elements(*self.All_PRODUCTS)

        for product in all_products:
            assert product.find_element(*self.PRODUCT_IMG).is_displayed(), 'Product image is missing'

            assert product.find_element(*self.PRODUCT_TITLE).text, 'Product title is missing'




