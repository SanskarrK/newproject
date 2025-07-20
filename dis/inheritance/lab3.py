class number:
    def __init__(self, num):
        self.num = num
    def __add__(self, num2):
        return self.num + num2.num

n = number(10)
m = number(20)

print(n + m)  # Output: 30