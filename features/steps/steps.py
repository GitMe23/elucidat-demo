from behave import *
import utilities

@given('I am on the BBC website')
def step_open_swag_login_page(context):
    utilities.navigate_to_root(context.driver)

