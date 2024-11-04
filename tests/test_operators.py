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

def test_addition_with_zero():
    # Arrange
    operation = "7+0+8"
    expected_value = 15

    # Act
    returned_value = Operators.Add(operation)

    # Assert
    assert returned_value == expected_value
