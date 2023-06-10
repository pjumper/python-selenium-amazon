# Created by user at 6/9/23
Feature: Customer Page Tests


  Scenario: Verify customer service page UI elements
    Given Open Amazon Customer Service Page
    Then Verify welcome text
    Then Verify 10 Customer Service links
    And Verify Search our help library text is present
    And Verify help library search field
    Then Verify All help topics texts is present
    Then Verify 11 Recommended Topics links