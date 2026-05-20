Feature: User Signup
    Scenario: Successful signup
        Given the user is on the Demoblaze home page
        When the user clicks on the signup link
        And enters a unique "<username>" and "<password>"
        And clicks signup button
        Then an alert should be displayed with message Sign up successful
        Examples:
            | username | password |
            | <random> | <random> |
