# Created by user at 6/4/23
Feature: Cart Tests


  Scenario: Cart is Empty
    Given Open Amazon Page
    When Click on cart
    Then Verify 0 in cart