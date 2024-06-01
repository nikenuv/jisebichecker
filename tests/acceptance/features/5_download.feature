@order5
Feature: Download Report
    Scenario: Successfully Checked Manuscript
        Given I am on Report Checked Manuscript Page
        When I press Download button
        Then the report file should be downloaded successfully
