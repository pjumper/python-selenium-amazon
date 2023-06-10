from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon Customer Service Page')
def open_cust_service_page(context):
    context.app.customer_service_page.open_cust_service_page()


@then('Verify welcome text')
def verify_welcome_texts(context):
    context.app.customer_service_page.verify_welcome_text()

@then('Verify {expected_links} Customer Service links')
def verify_cust_serv_links(context, expected_links):
    context.app.customer_service_page.verify_cust_serv_links(expected_links)


@then('Verify {expected_text} text is present')
def verify_search_library_text_present(context, expected_text):
    context.app.customer_service_page.verify_search_library_text_present(expected_text)


@then('Verify help library search field')
def verify_help_library_search_field(context):
    context.app.customer_service_page.verify_help_library_search_field()

@then('Verify {expected_text} texts is present')
def verify_help_topics_text_present(context, expected_text):
    context.app.customer_service_page.verify_help_topics_text_present(expected_text)


@then('Verify {expected_links} Recommended Topics links')
def verify_recommend_topic_links_present(context, expected_links):
    context.app.customer_service_page.verify_recommend_topic_links_present(expected_links)