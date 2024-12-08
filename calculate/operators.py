class Operators:
    def Add(numbers):
        parts = numbers.split('+')
        sum = 0
        for part in parts :
            number = int(part)
            sum += number
        return sum