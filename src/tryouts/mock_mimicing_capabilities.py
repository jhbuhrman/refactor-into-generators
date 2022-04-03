class SomeClass:
    def __init__(self):
        self._a = "hoi"

    def some_meth(self, b):
        print(f"{self._a=}, {b=}")
