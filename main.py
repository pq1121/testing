class Array:

    def __init__(self, *args):
        self.array = args

    def sum(self) -> float:
        summa = 0

        for i in self.array:
            summa += i

        return summa
    
    def multiply(self) -> float:
        multiply = 1
        
        for i in self.array:
            multiply *= i
        
        return multiply
    
    def average(self) -> float:
        return self.sum() / len(self.array)