Feature: Fibonacci's all the way

  Scenario Outline: List of first N Fibonacci numbers
    Given a module providing Fibonacci related functionality
    When the developer calls "first_n_fibs" with parameter "<number>"
    Then the function returns a list of "<fibonacci_numbers>"

  Examples:
    | number | fibonacci_numbers               |
    |      0 |                                 |
    |      1 | 0                               |
    |      2 | 0, 1                            |
    |      3 | 0, 1, 1                         |
    |      4 | 0, 1, 1, 2                      |
    |      5 | 0, 1, 1, 2, 3                   |
    |     10 | 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 |
