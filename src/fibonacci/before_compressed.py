import functools


def _check_nonnegative(f):
    @functools.wraps(f)
    def check_and_do(n):
        if n < 0:
            raise ValueError(f"n ({n!r}) should be a non-negative integer")
        return f(n)

    return check_and_do


def _check_positive(f):
    @functools.wraps(f)
    def check_and_do(n):
        if n < 1:
            raise ValueError(f"n ({n!r}) should be a positive integer")
        return f(n)

    return check_and_do


def fib_list_to(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


@_check_nonnegative
def fib_ordinal(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@_check_nonnegative
def first_n_fibs(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


@_check_positive
def largest_fib_less_than(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a


def smallest_fib_greater_equal(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a
