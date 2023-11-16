class Employee:
    def employeeDetails(self):         #Instance method
        self.name = "Ben"

    @staticmethod 
    def welcomeMessage():               #Static method. It does not take self p.
        print("Welcome to our organization!")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()
