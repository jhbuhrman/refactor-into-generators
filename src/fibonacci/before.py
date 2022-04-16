def fib_list_to(n: int) -> list[int]:
    """Return list of all Fibonacci numbers less than n."""
    result: list[int] = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def fib_ordinal(n: int) -> int:
    """Return the n'th Fibonacci number, counting from 0."""
    if n < 0:
        raise ValueError(f"n ({n!r}) should be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def first_n_fibs(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    if n < 0:
        raise ValueError(f"n ({n!r}) should be a non-negative integer")
    result: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def largest_fib_less_than(n: int) -> int:
    """Return largest Fibonacci number less than n."""
    if n < 1:
        raise ValueError(f"n ({n!r}) should be a positive integer")
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a


def smallest_fib_greater_equal(n: int) -> int:
    """Return smallest Fibonacci greater than or equal to n."""
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a
