Feature: Fibonacci functionality
  As a curious person,
  I want to see the a list of the Fibonacci numbers less than a certain
    value,
  So that I can learn how they look like.

  Scenario: List of Fibonacci numbers less than N
    Given a module providing Fibonacci related functionality
    When the developer calls the "fib_list_to" function with param "10"
    Then the function returns a list of "0, 1, 1, 2, 3, 5, 8"
