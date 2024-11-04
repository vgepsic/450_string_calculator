from calculate.operators import Operators

# Addition Tests


def test_addition_should_make_simple_addition():
    # arrange
    operation = "7+8"
    expected_value = 15
    # act
    returned_value = Operators.Add(operation)
    # assert
    assert returned_value == expected_value


def test_addition_with_non_numerical_values():
    # arrange
    operation = "a+b"
    expected_value = 0

    # act
    returned_value = Operators.Add(operation)

    # assert
    assert returned_value == expected_value
