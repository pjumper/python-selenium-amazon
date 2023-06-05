from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify {expected_count} in cart')
def verify_empty_cart(context, expected_count):
    context.app.cart_page.verify_cart_empty(expected_count)


