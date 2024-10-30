# String Calculator
Application simple réalisé dans le cadre du module 450.

## Spécifications produit

Application permetant de choisir une des opérations mathématiques suivantes :
- Addition
- Soustraction
- Multiplication
- Division

Et d'effectuer cette opération sur des chiffres en dessous de 1000.

Example pour une addition : “12+1+100+3” = 116

>### User story 1 : Addition
>
>En tant qu’utilisateur, je veux pouvoir fournir une chaîne de caractères contenant des nombres séparés par le signe +, afin que la fonction additionne uniquement les nombres valides (c’est-à-dire ceux qui sont inférieurs ou égaux à 1000) et ignore tout autre caractère ou nombre non valide.
>
>***Critères d'acceptation :***
>
>1. Somme correcte : La fonction doit retourner la somme de tous les nombres valides dans la chaîne d’entrée.
>2. Séparateur : Les nombres doivent être séparés par le signe + dans la chaîne d’entrée pour être additionnés.
>3. Limite de valeur : Les nombres supérieurs à 1000 doivent être ignorés dans le calcul.
>4. Valeurs non numériques : Si la chaîne contient des valeurs non numériques ou des erreurs de format, elles doivent être ignorées.
>
>Note :  Valeurs à ignorer = elles doivent être traitées comme 0 dans le calcul.


## Dépendances
- Python 3: [Python 3 download](https://www.python.org/downloads/)

## Installation

1. Installer un environment virtuel :
   - Creation de l'environment virtuel : `python -m venv venv`
   - Activation de l'environment virtuel:
     - Windows: `venv\Scripts\activate`
     - Unix/MacOS: `source venv/bin/activate`
   - ( Pour desactiver l'environment virtuel: `deactivate` )

2. Installation des dependances projet: `pip install -r requirements.txt`

## Exécution
1. Exécuter le script : `python main.py`
2. Exécuter les tests : `python -m pytest -v`
