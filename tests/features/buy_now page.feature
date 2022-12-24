Feature: Test Scenarios for buy now function

@smoke
  Scenario: User can input a negative number wiht warning message
    Given Go to CureSkin Hair Pro Solution
    When Input a negative number to the quntity field 
    And Click on Buy it now button
    Then A warning message for invalid quantity display 

# CureSkin Hair Pro Solution
