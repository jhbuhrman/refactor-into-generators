import unittest
import unittest.mock

import pytest_mock

from tryouts import mock_mimicing_capabilities


def test_mock_mimic_orig_class(mocker: pytest_mock.MockerFixture):

    SomeClassAlias = mock_mimicing_capabilities.SomeClass
    mocker.patch("tryouts.mock_mimicing_capabilities.SomeClass", autospec=True)
    # assert isinstance(mock_mimicing_capabilities.SomeClass, type)
    # assert issubclass(mock_mimicing_capabilities.SomeClass,
    #  SomeClassAlias)
    some_class_instance: (
        unittest.mock.NonCallableMagicMock | mock_mimicing_capabilities.SomeClass
    ) = mock_mimicing_capabilities.SomeClass()
    assert isinstance(some_class_instance, SomeClassAlias)
    assert isinstance(some_class_instance, unittest.mock.NonCallableMagicMock)
    print()
    print(f"{type(some_class_instance)=}")
    print(f"{some_class_instance.__class__=}")
    print(f"{some_class_instance.__class__.__mro__=}")
    some_class_instance.some_meth("b-param")
    print(
        f"{mock_mimicing_capabilities.SomeClass.return_value.some_meth.call_args_list=}"
    )
    mock_mimicing_capabilities.SomeClass.return_value.some_meth.assert_called_once()
    print(f"{some_class_instance=}")
