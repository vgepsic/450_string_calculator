class Operators:
    def Add(numbers):
        parts = numbers.split('+')
        sum = 0
        for part in parts :
            try :
                number = int(part)
            except :
                number = 0
            if number <= 1000 :
                sum += number
        return sum