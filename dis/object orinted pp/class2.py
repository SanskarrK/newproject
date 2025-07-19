class programmer:
    company = "Tech Innovations"
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

p = programmer("sanskar", 21, "Software Developer", 50000)
print(f"Name: {p.name}, Age: {p.age}, Position: {p.position}, Salary: {p.salary}")