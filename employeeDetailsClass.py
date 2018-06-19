class Employee:

    def __init__(self, fName, lName, pay):
        self.firstName = fName
        self.lastName = lName
        self.pay = pay
        self.email = fName + "." + lName + "@gmail.com"

    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

emp_1 = Employee("Patrick", "Hession", 20000)
emp_2 = Employee("Peter", "Hanly", 15000)

print(Employee.fullName(emp_2))

print(emp_1.email)
