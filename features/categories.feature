Feature: Product Categories

  Scenario: Verify Phones category

    Given user opens DemoBlaze website
    When user clicks Phones category
    Then phones category products should display


  Scenario: Verify Laptops category

    Given user opens DemoBlaze website
    When user clicks Laptops category
    Then laptops category products should display


  Scenario: Verify Monitors category

    Given user opens DemoBlaze website
    When user clicks Monitors category
    Then monitors category products should display