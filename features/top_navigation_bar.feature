Feature: Top Navigation Bar Functionality

  Background:
    Given the user is on the Demoblaze website homepage

  Scenario Outline: Verify navigation links that open homepage modals
    When the user clicks on the "<nav_link>" link in the top header
    Then a modal window titled "<modal_title>" should appear on the screen
    And the user closes the modal window

    Examples:
      | nav_link | modal_title |
      | Contact  | New message |
      | About us | About us    |
      | Log in   | Log in      |
      | Sign up  | Sign up     |

  Scenario: Verify the Cart link navigation redirect
    When the user clicks on the "Cart" link in the top header
    Then the user should be redirected to the page URL containing "cart.html"

  Scenario: Verify the Home link refreshes or returns to the main grid
    When the user clicks on the "Home" link in the top header
    Then the user should see the main product display grid reset or refreshed with all products visible