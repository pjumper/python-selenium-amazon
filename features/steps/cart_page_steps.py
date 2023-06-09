from selenium.webdriver.common.by import By
from behave import given, when, then



@when('Click no insurance button')
def click_no_insurance_bttn(context):
    context.app.cart_page.click_no_insurance_bttn()

@then('Verify {expected_count} in cart')
def verify_empty_cart(context, expected_count):
    context.app.cart_page.verify_cart_empty(expected_count)


