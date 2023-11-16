class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchivedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achived")
        else:
            print("Target has not been achived")


employeeOne = Employee()
print(employeeOne.name)
employeeOne.hasAchivedTarget()

employeeTwo = Employee()
employeeTwo.name = "John"
print(employeeTwo.name)
employeeTwo.hasAchivedTarget()