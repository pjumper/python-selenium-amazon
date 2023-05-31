from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import service

def browser_init(context, scenario):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
##############Drivers##############################

    context.driver = webdriver.Chrome('service=service')

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()