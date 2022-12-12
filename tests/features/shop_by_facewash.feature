Feature: Test Scenarios for shop by function

  @smoke
  Scenario: User can shop by product Face Washes
    Given Open Home page
    When Click Shop by product
    And Select Face Washes option
    Then Face Wash products display
