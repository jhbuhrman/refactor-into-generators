import itertools

def fib_list_or_ordinal(mode_is_list_to: bool, n: int) -> int | list[int]:
    if mode_is_list_to:
        result: list[int] = []
    a, b = 0, 1
    for i in itertools.count():
        if a >= n if mode_is_list_to else i >= n:
            break
        if mode_is_list_to:
            result.append(a)
        a, b = b, a + b
    return result if mode_is_list_to else a
