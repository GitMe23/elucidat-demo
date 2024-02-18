Feature: Finding the truth; Elucidat criminal justice training.

@truth-001
Scenario: The user can choose to explore the correct number of cases. 
Given I am on the start page
 When I click "START"
 Then I should see 3 case cards to choose from 

@truth-002
Scenario: 'Your score so far' displays the correct number
Given I am on the start page
 When I click "START"
 Then I can see that the score is 0

@truth-003 
Scenario Outline: Correct confirmation of user's vote
Given I am on the case selection page
  And I click on case: <case>
 When I submit: <vote>
 Then I should have the same vote confirmed in a pop-up window
Examples:
| case | vote       |
| 1    | GUILTY     |
| 2    | NOT GUILTY | 




