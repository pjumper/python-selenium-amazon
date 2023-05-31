from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon product B07BJKRR25')
def open_product_b0bbjrr25(context):
    context.app.product_page.open_product_b0bbjrr25()
