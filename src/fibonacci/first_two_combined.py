import itertools
from typing import cast

# fmt: off
def fib_list_or_ordinal(
    mode_is_list_to: bool, n: int
) -> int | list[int]:
    """The first two functions combined."""
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
# fmt: on


def fib_list_to(n: int) -> list[int]:
    """The 1st req'd functionality, implemented as combined (above)."""
    return cast(list[int], fib_list_or_ordinal(True, n))


def fib_ordinal(n: int) -> int:
    """The 2nd req'd functionality, implemented as combined (above)."""
    # Smuggling a bit here, do the `n >= 0` check up here, not in the
    # combined version, to keep the combined listing as short as
    # possible.
    if n < 0:
        raise ValueError(f"n ({n!r}) should be a non-negative integer")
    return cast(int, fib_list_or_ordinal(False, n))
