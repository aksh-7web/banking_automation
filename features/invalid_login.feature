Feature: Demoblaze Invalid Login Authentication

  Background:
    Given the user is on the Demoblaze website homepage

  Scenario Outline: Verify error messages for invalid login attempts
    When the user clicks on "Log in"
    And the user enters username "<username>" and password "<password>"
    And the user clicks the "Log in" button in the modal
    Then a browser alert pop-up should appear with the message "<error_message>"

    Examples:
      | username          | password       | error_message        |
      | non_existent_user | wrong_pass123  | User does not exist. |
      | admin             | incorret_pass  | Wrong password.      |