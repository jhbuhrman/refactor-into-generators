# fmt: off
def fib_list_to(n: int) -> list[int]:
    result: list[int] = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def fib_ordinal(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def first_n_fibs(n: int) -> list[int]:
    result: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def largest_fib_less_than(n: int) -> int:
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

def smallest_fib_greater_equal(n: int) -> int:
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a
# fmt: on


def _check_nonnegative(n):
    if n < 0:
        raise ValueError(f"n ({n!r}) should be a non-negative integer")


def _check_positive(n):
    if n <= 0:
        raise ValueError(f"n ({n!r}) should be a positive integer")
