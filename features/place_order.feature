Feature: Place Order

  Scenario: User places an order successfully
    Given user opens Demoblaze website
    When user adds a product to cart
    And user proceeds to checkout
    And user enters order details
    Then order should be placed successfully
