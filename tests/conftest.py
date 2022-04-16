from __future__ import annotations

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    import pytest

_FIB_MODULE_DFLT: Final = "refactored"


# https://docs.pytest.org/en/6.2.x/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options
def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--fib-module",
        action="store",
        default=_FIB_MODULE_DFLT,
        help=f"fib-module: the module basename containing the fibonacci functions (default: {_FIB_MODULE_DFLT!r})",
    )


# https://docs.pytest.org/en/6.2.x/example/simple.html#adding-info-to-test-report-header
def pytest_report_header(config: pytest.Config) -> str:
    return f"fib-module: {config.getoption('--fib-module')!r}"
