Feature: Fibonacci's all the way

  Scenario: List of first N Fibonacci numbers
    Given a module providing Fibonacci related functionality
    When the developer calls the "first_n_fibs" function with param "10"
    Then the function returns a list of "0, 1, 1, 2, 3, 5, 8, 13, 21, 34"

  Scenario: The largest Fibonacci number less than N
    Given a module providing Fibonacci related functionality
    When the dev calls "largest_fib_less_than" with param "100"
    Then the function returns the value "89"

  Scenario: The smallest Fibonacci number greater than or equal to N
    Given a module providing Fibonacci related functionality
    When the dev calls "smallest_fib_greater_equal" with param "100"
    Then the function returns the value "144"
