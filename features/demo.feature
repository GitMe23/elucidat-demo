Feature: Finding the truth; Elucidat criminal justice training.


@truth-001
Scenario: The user can choose to explore from the correct number of cases. 
Given I am on the landing page
 When I click START
 Then I should see 3 case tiles to choose from 

@truth-002
Scenario: The 'Score so far' displays zero on commencing
Given I am on the landing page
 When I click START
