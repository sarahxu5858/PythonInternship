Feature: Test Scenarios for buy now function

@smoke
  Scenario: User can input a negative number with warning message
    Given Go to CureSkin Hair Pro Solution
    When Input a 1 to the quantity field 
    And Click on Buy it now button
    Then Show order summary display

# CureSkin Hair Pro Solution
