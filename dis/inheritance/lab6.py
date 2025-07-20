class employee:
    salary = 50000
    increment = 5000

    @property
    def salary_after_increment(self):
        return (self.salary + self.salary * (self.increment / 100))

    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment = (salary - self.salary) / self.salary * 100

e = employee()
e.salary_after_increment = 60000
print(f"Updated Salary: {e.salary_after_increment}")  # Output: Updated Salary: 60000.0