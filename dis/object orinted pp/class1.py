class Employee:
    name = "John Doe"
    age = 30
    position = "Software Engineer"
    salary = 60000

john = Employee()
print(f"Name: {john.name}, Age: {john.age}, Position: {john.position}")

# here name is object attribute of class Employee and salary is also an object attribute.
# not class attributes because they are defined inside the class but outside any method.