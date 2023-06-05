from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon Page')
def open_main_page(context):
    context.app.main_page.open_main()

@when('Click Order Button')
def click_order_bttn(context):
    context.app.header.click_order_button()


@when('Click on cart')
def click_cart_button(context):
    context.app.header.click_cart_button()

@then('Verify Sign in page opened')
def verify_sign_in_shown(context):
    context.app.sign_in_page.sign_in_email()