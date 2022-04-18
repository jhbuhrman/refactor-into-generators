Feature: Largest Fib GreaterEqual N

  Scenario Outline: The smallest Fib number greater than or equal to N
    Given a module providing Fibonacci related functionality
    When the dev calls "smallest_fib_greater_equal" with param "<minim>"
    Then the function returns the value "<smallest_fib>"

    Examples:
      | minim | smallest_fib |
      | -1    | 0            |
      | 0     | 0            |
      | 1     | 1            |
      | 2     | 2            |
      | 3     | 3            |
      | 4     | 5            |
      | 143   | 144          |
      | 144   | 144          |
      | 145   | 233          |
