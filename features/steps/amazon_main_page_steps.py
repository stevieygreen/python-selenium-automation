from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Amazon Orders link')
def click_search(context):
    context.app.header.click_orders()


@when('Click on cart icon')
def click_search(context):
    context.app.header.click_cart()


@when('Click Orders')
def click_orders(context):
    context.app.header.click_orders()


@when('Hover over language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)


@when('Select department books')
def select_department(context):
    context.app.header.select_department()


@then('Verify {expected_result} text present')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'