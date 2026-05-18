Feature:  Login

    Scenario: Login works with the right details
        Given I open the ParaBank login page
        When I type in my correct username and password
        And I press the login button
        Then I should land on my Accounts Overview page

    Scenario: Login fails with the wrong details
        Given I open the ParaBank login page
        When I type in an incorrect username or password
        And I press the login button
        Then I should see a message saying the login could not be verified
