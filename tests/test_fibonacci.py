import dataclasses
import importlib
import types
from collections import abc
from typing import Callable, cast

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

# Scenarios

scenarios(
    "features/first_fibonacci.feature",
    "features/fibonaccis.feature",
    "features/fibonaccis2.feature",
    "features/more_fibonaccis.feature",
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
    parsers.parse('the dev calls "{function_name}" with param "{parameter:d}"'),
    target_fixture="fib_func_result",
)
def fib_func_result(fib_module, function_name: str, parameter: int) -> int | list[int]:
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
def step_impl(fib_func_result: int | list[int], expected_value: int):
    assert cast(int, fib_func_result) == expected_value
