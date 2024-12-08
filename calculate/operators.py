class Operators:
    @staticmethod
    def get_each_number(numbers: str):
        return numbers.split('+')
    
    @staticmethod
    def get_sum(numbers: list):
        result = 0
        for number in numbers:
            x = int(number)
            result += x
        return result

    @staticmethod
    def Add(input_str):
        numbers = Operators.get_each_number(input_str)
        sum = Operators.get_sum(numbers)
        return sum
