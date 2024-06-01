@order2
Feature: Sign in
    Scenario: Account doesn't exist
    Given i am on Sign In Page
    When I fill in "username" wih new username "testing_new"
    And I fill in "password" wih "88888888"
    And i press login button
    Then the response should contain Invalid Credentials

    Scenario: Sign In Success
    Given i am on Sign In Page
    When I fill in "username" wih existing username "testing"
    And I fill in "password" wih "88888888"
    And i press Login button
    Then i should be on Homepage