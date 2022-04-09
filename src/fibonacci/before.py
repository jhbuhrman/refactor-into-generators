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
        raise ValueError(
            f"n ({n!r}) should be greater than or equal to 0"
        )
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
