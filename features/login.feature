Feature: User Login
  Scenario: Successful login
    Given the user is on the Demoblaze home page
    When the user clicks on the login link
    And enters username "alok087" and password "tintin"
    And clicks login button
    Then user should see products page