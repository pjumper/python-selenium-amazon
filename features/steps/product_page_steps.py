from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon product B07BJKRR25')
def open_product_b0bbjrr25(context):
    context.app.product_page.open_product_b0bbjrr25()

@then('Verify user can see color options')
def verify_user_click_thru_colors(context):
    context.app.product_page.verify_user_can_click_thru_colors()
