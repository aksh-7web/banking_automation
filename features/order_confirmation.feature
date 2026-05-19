Feature: Order Confirmation

  Scenario: Verify order confirmation message
    Given user completed the purchase
    Then confirmation popup should appear
    And confirmation message should contain order id