class Operators:
    @staticmethod
    def _process_number(numbers: str, delimiter: str):
        result = 0
        for number in numbers.split(delimiter):
            try:
                x = int(number)
            except Exception:
                x = 0
            if 0 <= x <= 1000:
                if delimiter == "+":
                    result += x
                elif delimiter == "-":
                    result -= x
        return result

    # Opération Addition
    @staticmethod
    def Add(numbers):
        return Operators._process_number(numbers, "+")

    # Opération Soustraction
    @staticmethod
    def Subtract(numbers):
        return Operators._process_number(numbers, "-")
