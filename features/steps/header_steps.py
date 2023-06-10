from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon Page')
def open_main_page(context):
    context.app.main_page.open_main()
    sleep(3)

@when('Click Order Button')
def click_order_bttn(context):
    context.app.header.click_order_button()


@when('Click on cart')
def click_cart_button(context):
    context.app.header.click_cart_button()


@when('Click on Bestsellers Tab')
def click_bestseller_tab(context):
    context.app.header.click_bestsellers_tab()

@when('Click search button')
def click_search_button(context):
    context.app.header.click_search_button()


@when('Input text {text}')
def input_text_search_field(context, text):
    context.app.header.input_text_search_field(text)



@then('Verify Sign in page opened')
def verify_sign_in_shown(context):
    context.app.sign_in_page.sign_in_email()

@then('Verify {expected_links} Bestsellers Links are present')
def verify_bestseller_links_shown(context, expected_links):
    context.app.header.verify_bestseller_links_displayed(expected_links)



