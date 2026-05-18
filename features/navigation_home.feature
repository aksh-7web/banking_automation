Feature: Demoblaze Homepage Navigation

  Background:
    Given the user is on the Demoblaze website homepage

  Scenario: Verify the homepage structure
    Then the user should see the top logo "PRODUCT STORE"
    And the navigation bar should show links for "Home", "Contact", "About us", "Cart", "Log in" and "Sign up"

  Scenario Outline: Click on categories menu
    When the user clicks on "<category>" in the categories menu
    Then the page should show items like "<sample_item_1>" and "<sample_item_2>"

    Examples:
      | category | sample_item_1     | sample_item_2     |
      | Phones   | Samsung galaxy s6 | Nokia lumia 1520  |
      | Laptops  | Sony vaio i5      | MacBook air       |
      | Monitors | Apple monitor 24  | ASUS Full HD      |