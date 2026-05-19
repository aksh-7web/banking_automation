Feature: Demoblaze Duplicate Signup Verification

  Background:
    Given the user is on the Demoblaze website homepage

  Scenario: Verify error message when registering an existing user
    When the user clicks on "Sign up"
    And the user enters an already registered username "test" and password "password123"
    And the user clicks the "Sign up" button in the modal
    Then a browser alert pop-up should appear with the message "This user already exists."