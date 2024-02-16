from behave import *
import utilities

@given('I am on the landing page')
def step_open_swag_login_page(context):
    utilities.navigate_to_root(context.driver)
    
@step('I click {link_name}')
def step_click(context, link_name):
    utilities.clickById(context.driver, link_name)

@then('I should see {number_of_cases} case tiles to choose from')
def step_click(context, number_of_cases):
    pass