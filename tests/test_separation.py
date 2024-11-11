# Quentin Berthet - 4/11/2024
import pytest
from calculate.operators import Operators


def test_separator():
        # Arrange
        input_numbers = "4+5"
        expected_result = 9

        # Act
        result = Operators.Add(input_numbers)

        # Assert
        assert result == expected_result

