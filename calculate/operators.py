# pour le group "DRY" (Don't Repeat Yourself)
def calculate(expression: str, operator: str) -> int:
    if operator not in ['+', '-']:
        raise ValueError("Opérateur invalide. Utilisez '+' ou '-'.")

    # Séparer les nombres selon l'opérateur
    parts = expression.split(operator)
    
    try:
        # Initialiser le total avec le premier nombre
        total = int(parts[0]) if int(parts[0]) <= 1000 else 0
    except ValueError:
        total = 0

    for part in parts[1:]:
        try:
            # Convertir chaque partie en entier
            number = int(part)
            if number <= 1000:
                if operator == '+':
                    total += number
                elif operator == '-':
                    total -= number
        except ValueError:
            # Ignorer les parties non convertibles en entier
            pass
    
    return total
