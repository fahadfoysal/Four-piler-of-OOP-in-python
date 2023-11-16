class Employee:
    name = "Ben"

    def changeName(self):
        self.name = "John"

empOne = Employee()
print(empOne.name)
empOne.changeName()
print(empOne.name)
