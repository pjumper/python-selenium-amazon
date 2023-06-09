# Created by user at 5/30/23
Feature: Product Page Tests


  Scenario: User can see color options
    Given Open Amazon product B07BJKRR25
    Then Verify user can see color options

  Scenario: Verify user can see products and product names
    Given Open Amazon Page
    When Input text coffee
    When Click search button
    Then Verify every product has a name and image