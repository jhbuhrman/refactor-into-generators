@first_two
Feature: More Fibonacci's

  Scenario: A Fibonacci number with a negative ordinal
    Given a module providing Fibonacci related functionality
    When the dev attempts calling "fib_ordinal" with param "-1"
    Then a "ValueError" is raised matching "should be a non-negative integer"
