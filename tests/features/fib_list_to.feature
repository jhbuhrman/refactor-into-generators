@first_two
Feature: Fibonacci functionality
  As a Fibonacci interested person,
  I want to see a list of Fibonacci numbers less than a certain value,
  So that I can learn how they look like.

  Scenario Outline: List of Fibonacci numbers less than N
    Given a module providing Fibonacci related functionality
    When the developer calls "fib_list_to" with parameter "<limit>"
    Then the function returns a list of "<fibonacci_numbers>"

  Examples:
    | limit | fibonacci_numbers   |
    |     0 |                     |
    |     1 | 0                   |
    |     2 | 0, 1, 1             |
    |     3 | 0, 1, 1, 2          |
    |     4 | 0, 1, 1, 2, 3       |
    |     5 | 0, 1, 1, 2, 3       |
    |    10 | 0, 1, 1, 2, 3, 5, 8 |
