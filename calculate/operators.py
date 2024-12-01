class Operators:
    # Opération Addition
    def Add(numbers):
        # Séparer le string de input en parties
        parts = numbers.split('+')
        sum = 0
        # Traiter chaque partie du string
        for part in parts :
            try :
                number = int(part)
            except :
                number = 0
            if number <= 1000 and number >= 0 :
                # faire l'addition
                sum += number
        return sum

    # Opération Soustraction
    def Subtract(numbers):
        # Séparer le string de input en parties
        parts = numbers.split('-')
        sum = 0
        # Traiter chaque partie du string
        for part in parts :
            try :
                number = int(part)
            except :
                number = 0
            if number <= 1000 and number >= 0 :
                # faire la soustraction
                sum -= number
        return sum