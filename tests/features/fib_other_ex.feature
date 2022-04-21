# Please note: the argument checks have been removed from the
# implementation; these Features are not tested anymore.

Feature: Fibonacci exceptions from the final three

  Scenario Outline: A Fibonacci function raises
    Given a module providing Fibonacci related functionality
    When the dev attempts calling "<fib_function>" with param "<n>"
    Then a "<exception>" is raised matching "<pattern>"

  Examples:
    | fib_function          | n  | exception  | pattern              |
    | first_n_fibs          | -1 | ValueError | non-negative integer |
    | largest_fib_less_than |  0 | ValueError | positive integer     |
