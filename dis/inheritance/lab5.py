class animals:
    pass

class pet(animals):
    pass

class dog(pet):
    @staticmethod
    def bark():
        print("Woof, woof!")

d = dog()
d.bark()  # Output: Woof, woof!