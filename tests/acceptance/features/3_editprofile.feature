@order7
Feature: Edit Profile
    Scenario: Already Logged In
    Given i am on Logged In Homepage
    When i press User Profile button
    And i press Edit Profile button
    Then i should be on Edit Profile Page
    When I enter a new email and username in the Edit Profile fields
    And i press Save button
    Then i should be on Edit Profile Page