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

def test_addition_with_other_separator_than_plus():
    # arrange
    operation = "5*5"
    expected_value = 0
    # act
    returned_value = Operators.Add(operation)
    # assert
    assert returned_value == expected_value

def test_separator_plus_is_good():
    # arrange
    operation = "5+5"
    expected_value = 10
    # act
    returned_value = Operators.Add(operation)
    # assert
    assert returned_value == expected_value

# Separator Tests

def test_separator_when_too_much_separator_should_ignore_second_separator():
    # arrange
    operation = "27++38"
    expected_value = 65
    # act
    returned_value = Operators.Add(operation)
    # assert
    assert returned_value == expected_value


