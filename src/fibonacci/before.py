

def fib_list_to(n: int) -> list[int]:
    """Return list of all Fibonacci numbers less than n."""
    result: list[int] = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
