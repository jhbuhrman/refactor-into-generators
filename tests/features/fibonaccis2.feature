Feature: Fibonacci's all the way
  As a curious person,
  I would like to know the N'th Fib number
  So that I can learn how they look like.

  Scenario Outline: The N'th Fibonacci number
    Given a module providing Fibonacci related functionality
    When I call the "fib_ordinal" function with parameter <ordinal>
    Then the function returns the value <fibonacci_number>

  Examples:
    | ordinal | fibonacci_number |
    |       0 |                0 |
    |       1 |                1 |
    |       2 |                1 |
    |       3 |                2 |
    |       9 |               32 |
    |      78 | 8944394323791464 |
