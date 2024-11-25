class Operators:
    # Opération Addition
    def Add(numbers):
        sum = 0
        # Traiter chaque partie du string
        for part in numbers.split('+'):
            try :
                number = int(part)
            except :
                number = 0
            if number <= 1000:
                # faire l'addition
                sum += number
        return sum

    # Opération Soustraction
    def Subtract(numbers):
        sum = 0
        # Traiter chaque partie du string
        for part in numbers.split('-'):
            try :
                number = int(part)
            except :
                number = 0
            if number <= 1000:
                # faire la soustraction
                sum -= number
        return sum
