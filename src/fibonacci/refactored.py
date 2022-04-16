# fib_funcs.py

from itertools import dropwhile, islice, takewhile

from more_itertools import first, last, one


def fib_gen():
    """Generate an endless sequence of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_list_to(n):
    return list(takewhile(lambda value: value < n, fib_gen()))


def fib_ordinal(n):
    return one(islice(fib_gen(), n, n + 1))


def first_n_fibs(n):
    return list(islice(fib_gen(), n))


def largest_fib_less_than(n):
    return last(takewhile(lambda value: value < n, fib_gen()), None)


def smallest_fib_greater_equal(n):
    return first(dropwhile(lambda value: value < n, fib_gen()), None)
