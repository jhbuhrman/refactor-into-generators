import functools
import importlib
import types
from typing import Any, Callable, cast

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

# Scenarios

scenarios(
    "features/fib_list_to.feature",
    "features/fib_ordinal.feature",
    "features/fib_ordinal_ex.feature",
    "features/fib_other_ex.feature",
    "features/first_n_fibs.feature",
    "features/largest_fib_less_than.feature",
    "features/smallest_fib_greater_equal.feature",
)


@given(
    "a module providing Fibonacci related functionality", target_fixture="fib_module"
)
def fib_module(request: pytest.FixtureRequest) -> types.ModuleType:
    fib_module_name = request.config.getoption("--fib-module")
    return importlib.import_module(f"fibonacci.{fib_module_name}")


@when(
    parsers.parse(
        'the developer calls the "{function_name}" function with param "{parameter:d}"'
    ),
    target_fixture="fib_func_result",
)
@when(
    parsers.parse(
        'the developer calls "{function_name}" with parameter "{parameter:d}"'
    ),
    target_fixture="fib_func_result",
)
@when(
    parsers.parse('the dev calls "{function_name}" with param "{parameter:d}"'),
    target_fixture="fib_func_result",
)
def fib_func_result(
    fib_module: types.ModuleType, function_name: str, parameter: int
) -> int | list[int]:
    # get the desired functiom from the designated module
    fib_function: Callable[[int], int | list[int]] = getattr(fib_module, function_name)
    return fib_function(parameter)


@then(
    parsers.cfparse(
        'the function returns a list of "{expected_int_sequence:Number*}"',
        extra_types=dict(Number=int),
    )
)
def step_impl(
    fib_func_result: int | list[int], expected_int_sequence: list[int]
) -> None:
    assert cast(list[int], fib_func_result) == expected_int_sequence


@then(parsers.parse('the function returns the value "{expected_value:d}"'))
def step_impl(fib_func_result: int | list[int], expected_value: int) -> None:
    assert cast(int, fib_func_result) == expected_value


@when(
    parsers.parse('the dev attempts calling "{function_name}" with param "{param:d}"'),
    target_fixture="fib_func_callable",
)
def fib_func_callable(
    fib_module: types.ModuleType, function_name: str, param: int
) -> Callable[[], int | list[int]]:
    fib_function: Callable[[int], int | list[int]] = getattr(fib_module, function_name)
    return functools.partial(fib_function, param)


@then(parsers.parse('a "{exception_clsname}" is raised matching "{pattern}"'))
def step_impl(
    fib_func_callable: Callable[[], int | list[int]],
    exception_clsname: str,
    pattern: str,
) -> None:
    exception_cls = _get_exception_cls_by_name(exception_clsname)
    with pytest.raises(exception_cls, match=pattern):
        fib_func_callable()


def _get_exception_cls_by_name(exception_clsname: str) -> type[Exception]:
    module_str, sep, exception_basename = exception_clsname.partition(":")
    if not sep:
        module_str, sep, exception_basename = exception_clsname.rpartition(".")
    if not sep:
        module_str = "builtins"
    module = importlib.import_module(module_str)
    if "." in exception_clsname:
        raise ValueError(
            f"nested symbols ({exception_clsname!r}) are not supported yet"
        )
    exception_cls = getattr(module, exception_clsname)
    if not issubclass(exception_cls, Exception):
        raise TypeError(f"{exception_cls!r} is not a subclass of Exception")
    return exception_cls
