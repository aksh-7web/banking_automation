Feature: Place Order Functionality

  Scenario: User places order successfully

    Given the user is on the Demoblaze home page

    When the user selects product "Samsung galaxy s6"

    And the user adds product to cart

    And the user opens cart

    And the user clicks place order button

    And the user enters name "Pratyush", country "India", city "Bhubaneswar", card "12345678", month "05", year "2026"

    And the user clicks purchase button

    Then order should be placed successfully