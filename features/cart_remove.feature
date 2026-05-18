Feature: Remove products from cart in DemoBlaze

  Scenario: Remove a product from the cart
    Given the user launches the DemoBlaze website
    And the user has added "Samsung galaxy s6" to the cart
    When the user navigates to the cart page
    And the user removes "Samsung galaxy s6" from the cart
    Then the product "Samsung galaxy s6" should not be displayed in the cart

  Scenario: Verify cart total after removing a product
    Given the user launches the DemoBlaze website
    And the user has added "Samsung galaxy s6" to the cart
    And the user has added "Nokia lumia 1520" to the cart
    When the user navigates to the cart page
    And the user removes "Samsung galaxy s6" from the cart
    Then the cart total should be updated correctly

  Scenario: Remove all products from the cart
    Given the user launches the DemoBlaze website
    And the user has added "Samsung galaxy s6" to the cart
    And the user has added "Nokia lumia 1520" to the cart
    When the user navigates to the cart page
    And the user removes "Samsung galaxy s6" from the cart
    And the user removes "Nokia lumia 1520" from the cart
    Then the cart should be empty