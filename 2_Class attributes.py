class Employee:
    numberOfWorkingHours = 40

employeeOne = Employee()
employeeTwo = Employee()
print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

Employee.numberOfWorkingHours = 45
print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

employeeOne.name = "John"
print(employeeOne.name)

employeeTwo.name = "Mary"
print(employeeTwo.name)

employeeOne.numberOfWorkingHours = 40
print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)