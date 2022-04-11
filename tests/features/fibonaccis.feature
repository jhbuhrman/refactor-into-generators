Feature: More Fibonacci's
  As a curious person,
  I want to see a list of Fibonacci numbers less than a certain value,
    and would like to know the N'th Fib number
  So that I can learn how they look like.

  Scenario: List of first N Fibonacci numbers
    Given a module providing Fibonacci related functionality
    When the developer calls the "fib_list_to" function with param "10"
    Then the function returns a list of "0, 1, 1, 2, 3, 5, 8"

  Scenario: The N'th Fibonacci number (counting from 0)
    Given a module providing Fibonacci related functionality
    When the developer calls the "fib_ordinal" function with param "9"
    Then the function returns the value "34"
