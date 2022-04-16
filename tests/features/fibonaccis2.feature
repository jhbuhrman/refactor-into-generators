@first_two
Feature: More Fibonacci's

  Scenario Outline: The N'th Fibonacci number (ordinal counting from 0)
    Given a module providing Fibonacci related functionality
    When the dev calls "fib_ordinal" with param "<ordinal>"
    Then the function returns the value "<fibonacci_number>"

  Examples:
    | ordinal | fibonacci_number |
    |       0 |                0 |
    |       1 |                1 |
    |       2 |                1 |
    |       3 |                2 |
    |       4 |                3 |
    |       5 |                5 |
    |       6 |                8 |
    |       9 |               34 |
    |      78 | 8944394323791464 |
