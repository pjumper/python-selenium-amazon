from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify hamburger menu is present')
def verify_ham_menu_shown(context):
    context.app.main_page.verify_ham_menu_present()


@then('Verify Footer has {expected_count} links')
def verify_footer_link_count(context, expected_count):
    context.app.main_page.verify_footer_link_count(expected_count)


@then('Verify Header has {expected_count} links')
def verify_header_link_count(context, expected_count):
    context.app.main_page.verify_header_link_count(expected_count)
