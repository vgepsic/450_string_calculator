from calculate.operators import Operators
import pytest

# Addition Tests

def test_addition_should_make_simple_addition():
    # arrange
    operation = "7+8"
    expected_value = 15
    # act
    returned_value = Operators.Add(operation)
    # assert
    assert returned_value == expected_value


