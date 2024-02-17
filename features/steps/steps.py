import time
from behave import *
import utilities

@given('I am on the start page')
def step_open_start_page(context):
    utilities.navigate_to_root(context.driver)

@when('I click {string}')
def step_when(context, string) :
    utilities.click_by_id(context.driver, string.strip('"'))

@then('I should see {int} case cards to choose from')
def step_then(context, int) :
    expected = int
    actual = utilities.get_number_of_cards_on_page(context.driver)
    assert actual == expected, f'Cases on page: {actual}, expected {expected}'

@then('I should see {string}')
def step_then(context, string) :
    assert string.strip('"') in context.driver.page_source, f'{string} not found on page'

@then('I can see that the score is {int}')
def step_then(context, int) :
    expected_text = f'Your score so far: {int}'
    actual_text = utilities.get_score_text_on_page(context.driver)
    assert actual_text == expected_text, f'Expected "{expected_text}", "{actual_text}" on page'

@given('I am on the case selection page')
def step_open_start_page(context):
    utilities.navigate_to_root(context.driver)
    utilities.click_by_id(context.driver, 'START')

@given('I click on case: {case_number}')
def step_click_case(context, case_number):
    utilities.click_by_id(context.driver, f'CASE_{case_number}')

@when('I submit: {vote}')
def step_when(context, vote) :
    context.vote = vote.strip('"')
    utilities.click_by_id(context.driver, 'JUDGE THIS')
    time.sleep(1)
    utilities.click_by_id(context.driver, context.vote)
    time.sleep(1)
    utilities.click_by_id(context.driver, 'VOTE')
    time.sleep(1)

@then('I should have the same vote confirmed in a pop-up window')
def step_then(context) :
    expected = f'{context.vote}!'
    actual = utilities.get_vote_confirmation_on_page(context.driver)
    assert actual == expected, f'Expected "{expected}", Actual: "{actual}"'
    time.sleep(1)




    





