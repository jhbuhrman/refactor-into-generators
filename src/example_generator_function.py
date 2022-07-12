from collections.abc import Iterator


def gen2() -> Iterator[int]:
    """Like `iter(range(2))`."""
    print(" [==before yield 0==]")
    yield 0
    print(" [==before yield 1==]")
    yield 1
    print(" [==before return==]")
