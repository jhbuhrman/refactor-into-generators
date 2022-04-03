
class before:

    

    @staticmethod
    def fib_list_to(n: int) -> list[int]:
        """Return list of all Fibonacci number less than n."""
        retval: list[int] = []
        a, b = 0, 1
        while a < n:
            retval.append(a)
            a, b = b, a + b
        return retval
