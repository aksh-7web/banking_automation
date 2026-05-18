Feature: Product Categories Functionality

  Scenario: Verify Phones category products

    Given user opens DemoBlaze website
    When user clicks Phones category
    Then phone products should display successfully


  Scenario: Verify Laptops category products

    Given user opens DemoBlaze website
    When user clicks Laptops category
    Then laptop products should display successfully


  Scenario: Verify Monitors category products

    Given user opens DemoBlaze website
    When user clicks Monitors category
    Then monitor products should display successfully