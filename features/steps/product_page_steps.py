from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon product B07BJKRR25')
def open_product_b0bbjrr25(context):
    context.app.product_page.open_product_b0bbjrr25()



@when('Click on first product')
def click_first_product(context):
    context.app.product_page.click_first_product()

@when('Click on Add to cart button')
def add_to_cart(context):
    context.app.product_page.add_to_cart()

@when('Open Cart Page')
def click_cart_bttn(context):
    context.app.product_page.click_cart()



@then('Verify user can see color options')
def verify_user_click_thru_colors(context):
    context.app.product_page.verify_user_can_click_thru_colors()

@then('Verify every product has a name and image')
def verify_product_name_images(context):
    context.app.product_page.verify_product_name_image()


@then('Verify that text {expected_result} is displayed')
def verify_product_displayed(context, expected_result):
    context.app.product_page.verify_product_displayed(expected_result)
