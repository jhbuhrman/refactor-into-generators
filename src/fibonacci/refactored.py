import itertools
from typing import Iterator

import more_itertools


def fib_gen() -> Iterator[int]:
    """Generate an endless sequence of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_list_to(n: int) -> list[int]:
    """Return list of all Fibonacci numbers less than n."""
    return list(itertools.takewhile(lambda fib: fib < n, fib_gen()))


def fib_ordinal(n: int) -> int:
    """Return the n'th Fibonacci number, counting from 0."""
    try:
        return more_itertools.one(itertools.islice(fib_gen(), n, n + 1))
    except ValueError as e:
        raise ValueError(f"n ({n!r}) should be a non-negative integer") from e


def first_n_fibs(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    try:
        return list(itertools.islice(fib_gen(), n))
    except ValueError as e:
        raise ValueError(f"n ({n!r}) should be a non-negative integer") from e


def largest_fib_less_than(n: int) -> int:
    """Return largest Fibonacci number less than n."""
    try:
        return more_itertools.last(itertools.takewhile(lambda fib: fib < n, fib_gen()))
    except ValueError as e:
        raise ValueError(f"n ({n!r}) should be a positive integer") from e


def smallest_fib_greater_equal(n: int) -> int:
    """Return smallest Fibonacci greater than or equal to n."""
    return more_itertools.first(
        itertools.dropwhile(lambda fib: fib < n, fib_gen()), None
    )
