Feature: Largest Fib Less Than N

  Scenario Outline: The largest Fibonacci number less than N
    Given a module providing Fibonacci related functionality
    When the dev calls "largest_fib_less_than" with param "<limit>"
    Then the function returns the value "<largest_fib>"

  Examples:
    | limit | largest_fib |
    |     1 |           0 |
    |     2 |           1 |
    |     3 |           2 |
    |     5 |           3 |
    |     6 |           5 |
    |   143 |          89 |
    |   144 |          89 |
    |   145 |         144 |
