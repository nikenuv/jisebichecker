@order1
Feature: Registration
    Scenario: Password Doesn't Match
        Given I am on Register Page
        When I fill in "email" wih new email "testing@gmail.com"
        And I fill in "username" wih new username "testing"
        And I fill in "password" wih "88888888"
        And I fill in "confirm_password" with "88888889"
        And I press Sign Up button
        Then the response should contain Password does not match
        And I should be on Register Page    

    Scenario: Registration Success
        Given I am on Register Page
        When I fill in "email" wih new email "testing@gmail.com"
        And I fill in "username" wih new username "testing"
        And I fill in "password" wih "88888888"
        And I fill in "confirm_password" with "88888888"
        And I press Sign Up button
        Then I should be on SignIn Page

    Scenario: Username already exists
        Given I am on Register Page
        When I fill in "email" wih new email "testing1@gmail.com"
        And I fill in "username" wih existing username "testing"
        And I fill in "password" wih "88888888"
        And I fill in "confirm_password" with "88888888"
        And I press Sign Up button
        Then the response should contain Username already exists
        And I should be on Register Page

