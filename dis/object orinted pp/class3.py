class claculator:
    def __init__(self, num1):
        self.num1 = num1

    def square(self):
        print(f"Square of {self.num1} is {self.num1 ** 2}")
    def cube(self):
        print(f"Cube of {self.num1} is {self.num1 ** 3}")
    def square_root(self):
        print(f"Square root of {self.num1} is {self.num1 ** 0.5}")

a = claculator(5)
a.square()
a.cube()
a.square_root()