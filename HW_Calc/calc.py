class Calc:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b
        else:
            print("division by 0 is not allowed")
            return None

    @staticmethod
    def degree(a, b):
        return a ** b

    @staticmethod
    def remainder(a, b):
        return a % b

