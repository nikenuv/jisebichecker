@order3
Feature: Upload Manuscript
    Scenario: Upload Manuscript Success
    Given I am on Upload Manuscript Page
    When I upload .docx Manuscript file on Upload field
    And I press Check Now! button
    Then I should be on Report Page

    Scenario: Wrong Uploaded File Type
    Given I am on Upload Manuscript Page
    When I upload .pdf Manuscript file on Upload field
    And I press Check Now! button
    Then I should be on Upload Manuscript Page