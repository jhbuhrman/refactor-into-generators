import dataclasses
import types
from collections import abc
from typing import Any

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

# Scenarios

scenarios("features/first_fibonacci.feature", "features/fibonaccis.feature")


@dataclasses.dataclass()
class TestState:
    function_name: str | None = None
    args: tuple | None = ()
    kwargs: dict | None = dataclasses.field(default_factory=dict)
    return_value: Any = None


@pytest.fixture
def module() -> types.ModuleType:
    from fibonacci import before

    return before


@pytest.fixture
def state() -> abc.Iterator[TestState]:
    test_state = TestState()
    yield test_state


@given("a module providing Fibonacci related functionality")
def step_impl() -> None:
    pass


@when(
    parsers.parse(
        'I call the "{function_name}" function with parameter "{parameter:d}"'
    )
)
def step_impl(
    module: types.ModuleType, state: TestState, function_name: str, parameter: int
) -> None:
    state.function_name = function_name
    state.args = (parameter,)
    function = getattr(module, function_name)
    state.return_value = function(*state.args)


@then(
    parsers.cfparse(
        'the function returns a list of "{int_sequence:Number*}"',
        extra_types=dict(Number=int),
    )
)
def step_impl(state: TestState, int_sequence: list[int]) -> None:
    assert state.return_value == int_sequence


@then(parsers.parse('the function returns the value "{expected_value:d}"'))
def step_impl(state: TestState, expected_value: int):
    assert state.return_value == expected_value


@when('I call the "fib_ordinal" function with parameter <ordinal>')
def step_impl():
    raise NotImplementedError(
        u'STEP: When I call the "fib_ordinal" function with parameter <ordinal>')


@then("the function returns the value <fibonacci_number>")
def step_impl():
    raise NotImplementedError(u'STEP: Then the function returns the value <fibonacci_number>')
