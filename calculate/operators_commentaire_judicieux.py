class Operators:
    def Add(numbers: str) -> int:
        parts = numbers.split('+')
        sum = 0
        for part in parts :
            try :
                number = int(part)
            except :
                number = 0
            if number <= 1000 and number >= 0 :
                sum += number
        return sum

    def Subtract(numbers: str) -> int:
        parts = numbers.split('-')
        # sum will store the total of subtraction.
        sum = 0
        for part in parts :
            try :
                number = int(part)
            except :
                number = 0
            if number <= 1000 and number >= 0 :
                sum -= number
        return sum
