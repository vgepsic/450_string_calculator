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
