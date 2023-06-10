# Created by user at 6/4/23
Feature: Cart Tests


  Scenario: Cart is Empty
    Given Open Amazon Page
    When Click on cart
    Then Verify 0 in cart

  Scenario: User can add a product to cart
    Given Open Amazon Page
    When Input text Core Fitness Adjustable Dumbbells
    When Click search button
    And Click on first product
    And Click on Add to cart button
    When Click no insurance button
    And Open Cart Page
    Then Verify cart has 1 item
