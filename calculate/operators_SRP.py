class Operators:
    # Opération Addition
    def Add(self, numbers):
        # Récupérer les parties du string
        parts = self.GetParts(numbers, '-')

        # Calculer la somme finale
        sum = self.GetSum(parts, '+')

        return sum

    # Opération Soustraction
    def Subtract(self, numbers):
        # Récupérer les parties du string
        parts = self.GetParts(numbers, '-')

        # Calculer la somme finale
        sum = self.GetSum(parts, '-')

        return sum
    
    def GetParts(self, numbers: int, operator: str):
        # Séparer le string de input en parties
        return numbers.split(operator)
    
    def GetSum(self, parts: list, operator: str):
         # Traiter chaque partie du string
        sum = 0
        for part in parts:
            try:
                number = int(part)
            except:
                number = 0
            if number <= 1000 and number >= 0:
                match(operator):
                    case '+':
                        sum += number
                    case '-':
                        sum -= number
        return sum