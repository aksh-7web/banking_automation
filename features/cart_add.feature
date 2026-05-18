Feature: Add products to cart in DemoBlaze

  Scenario: Add a single product to the cart
    Given the user launches the DemoBlaze website
    When the user selects the product "Samsung galaxy s6"
    And the user adds the product to the cart
    Then the product should be added successfully
    When the user navigates to the cart page
    Then the cart should display "Samsung galaxy s6"

  Scenario: Add multiple products to the cart
    Given the user launches the DemoBlaze website
    When the user selects the product "Samsung galaxy s6"
    And the user adds the product to the cart
    And the user returns to the home page
    And the user selects the product "Nokia lumia 1520"
    And the user adds the product to the cart
    When the user navigates to the cart page
    Then the cart should display "Samsung galaxy s6"
    And the cart should display "Nokia lumia 1520"

  Scenario: Verify cart total after adding a product
    Given the user launches the DemoBlaze website
    When the user selects the product "Samsung galaxy s6"
    And the user adds the product to the cart
    When the user navigates to the cart page
    Then the cart total should be updated correctly