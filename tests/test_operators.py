from calculate.operators import Operators

# Addition Tests

################# Critère d'acceptation phase 1 : somme correcte #################
## Scénario 1 : somme de deux nombres
def test_addition_should_make_simple_addition():
    # arrange
    operation = "7+8"
    expected_value = 15
    # act
    returned_value = Operators.Add(operation)
    # assert
    assert returned_value == expected_value

## Scénario 2 : somme de plus de deux nombres
def test_addition_should_make_simple_addition_with_more_than_two_numbers():
    # arrange
    operation = "9+5+3+46+97+5"
    expected_value = 165
    
## Scénario 3 : somme du plus grand nombre admissible avec un autre chiffre valide
def test_addition_should_make_simple_addition_with_the_highest_possible_number():
    # arrange
    operation = "999+1"
    expected_value = 1000
    # act
    returned_value = Operators.Add(operation)
    # assert
    assert returned_value == expected_value
############################### Fin de la phase 1 ################################

def test_addition_with_non_numerical_values():
    # arrange
    operation = "a+b"
    expected_value = 0

    # act
    returned_value = Operators.Add(operation)

    # assert
    assert returned_value == expected_value

    # groupe 2

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
