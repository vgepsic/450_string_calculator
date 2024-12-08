from calculate.operators import Operators
import pytest

# Addition Tests

# TDD: iteration 1
# arrange
@pytest.mark.parametrize("operation, expected_value", [
    ("7+8", 15),
    ("1+2+3+4", 10),
    ("1+2+0", 3),
    ("0", 0),
    ("1+2+3+4+5+6+7+8+9+10+11+12+300", 378),
])
def test_should_make_addition(operation, expected_value):
    # act
    returned_value = Operators.Add(operation)
    # assert
    assert returned_value == expected_value

