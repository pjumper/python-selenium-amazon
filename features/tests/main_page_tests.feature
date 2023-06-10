# Created by user at 6/9/23
Feature: Main Page Tests


  Scenario: User can see on hamburger menu
    Given Open Amazon Page
    Then Verify hamburger menu is present


  Scenario: Verify Footer Links
    Given Open Amazon Page
    Then Verify Footer has 42 links
    Then Verify Header has 29 links