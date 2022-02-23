from typing import Final

import pytest

_FIRST_TWO_MARK = "first_two"
_FIB_MODULE_FIRST_TWO_COMBINED = "first_two_combined"
_FIB_MODULE_DFLT: Final = "refactored"
# : Final =


# https://docs.pytest.org/en/6.2.x/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options
def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--fib-module",
        action="store",
        default=_FIB_MODULE_DFLT,
        help=(
            "fib-module: the module basename containing the fibonacci functions"
            f" (default: {_FIB_MODULE_DFLT!r})"
        ),
    )


# https://docs.pytest.org/en/6.2.x/example/simple.html#adding-info-to-test-report-header
def pytest_report_header(config: pytest.Config) -> str:
    return f"fib-module: {config.getoption('--fib-module')}"


# https://docs.pytest.org/en/6.2.x/example/simple.html#control-skipping-of-tests-according-to-command-line-option
def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    if config.getoption("--fib-module") != _FIB_MODULE_FIRST_TWO_COMBINED:
        return
    skip_not_implemented = pytest.mark.skip(
        reason=(
            f"is not marked @{_FIRST_TWO_MARK} and"
            f" fib-module == {_FIB_MODULE_FIRST_TWO_COMBINED!r}"
        )
    )
    for item in items:
        if (_FIRST_TWO_MARK) not in item.keywords:
            item.add_marker(skip_not_implemented)


# https://docs.pytest.org/en/stable/how-to/mark.html#registering-marks
def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers", "first_two: the to be tested function is one of the first two"
    )
