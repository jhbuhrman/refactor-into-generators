Feature: Fibonacci's all the way
  As a curious person,
  I want to see the a list of the Fibonacci numbers less than a certain
    value, and would like to know the N'th Fib number
  So that I can learn how they look like.

  Scenario: List of Fibonacci numbers less than N
    Given a module providing Fibonacci related functionality
    When I call the "fib_list_to" function with parameter "10"
    Then the function returns a list of "0, 1, 1, 2, 3, 5, 8"

  Scenario: The N'th Fibonacci number
    Given a module providing Fibonacci related functionality
    When I call the "fib_ordinal" function with parameter "9"
    Then the function returns the value "34"
