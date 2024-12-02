class Operators:
    # Opération Addition
    def Add(operation):
        # Séparer le string de input en parties
        numbers = operation.split('+')
        sum = 0
        # Traiter chaque partie du string
        for number in numbers :
            try :
                number = int(number)
            except :
                number = 0
            if number <= 1000 and number >= 0 :
                # faire l'addition
                sum += number
        return sum

    # Opération Soustraction
    def Subtract(operation):
        # Séparer le string de input en parties
        numbers = operation.split('-')
        sum = 0
        # Traiter chaque partie du string
        for number in numbers :
            try :
                number = int(number)
            except :
                number = 0
            if number <= 1000 and number >= 0 :
                # faire la soustraction
                sum -= number
        return sum