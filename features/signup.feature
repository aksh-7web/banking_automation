Feature: User Signup
    Scenario: Successful signup
        Given the user is on the Demoblaze home page
        When the user clicks on the signup link
        And enters username "newUser123" and password "newPass123"
        Then an alert should be displayed with message "Sign up successful."
