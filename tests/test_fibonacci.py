import dataclasses
from collections import abc
from typing import Any
import types

import pytest
from pytest_bdd import scenarios, given, when, then, parsers


# Scenarios

scenarios('features/fibonacci.feature')


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

@when(parsers.parse('I call the "{function_name}" function with parameter "{parameter:d}"'))
def step_impl(module: types.ModuleType, state: TestState, function_name: str, parameter: int) -> None:
    state.function_name = function_name
    state.args = (parameter,)
    function = getattr(module, function_name)
    state.return_value = function(*state.args)


@then(parsers.parse('the function returns a list of "{int_sequence_s}"'))
def step_impl(state: TestState, int_sequence_s: str) -> None:
    expected_ints = [int(s.strip()) for s in int_sequence_s.split(",")]
    assert state.return_value == expected_ints
