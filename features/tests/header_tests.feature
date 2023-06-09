# Created by user at 6/5/23
Feature: Header Tests


  Scenario: Verify BestSellers Link
    Given Open Amazon Page
    When Click on Bestsellers Tab
    Then Verify 5 Bestsellers Links are present

  Scenario: Verify Footer Links
    Given Open Amazon Page
    Then Verify Footer has 42 links