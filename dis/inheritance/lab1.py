
class employee:
    company = "TechCorp"
    name = "John Doe"
    def show(self):
        print(f"ther name is {self.name} and company is {self.company}")

class coder:
        language = "Python"
        def showlanguage(self):
            print(f"the language is {self.language}")

class programmer(employee,coder):
    company = "CodeInc"
    def languageshow(self):
        print(f"the name is {self.name} and company is {self.company} and language is {self.language}")

a = employee()
b = programmer()
b.show()
b.languageshow()
b.showlanguage()