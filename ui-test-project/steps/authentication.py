from behave import given, when, then
from pages.login_page import LoginPage


@given("I am on login page")
def step_implementation(context):
    context.driver.get(context.url)


@when('I log in as "{user}"')
def step_implementation(context, user):
    context.login_page = LoginPage(context.driver)
    context.login_page.login(context.credentials[user]["email"],
                             context.credentials[user]["password"])


@then('I see an error message')
def step_implementation(context):
    returned_message = context.login_page.find_error_message()
    assert returned_message == context.login_error_message
