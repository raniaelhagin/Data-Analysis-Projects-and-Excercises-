# Class Variables
class Employee:

    # class variable, could be accessed using the class itself or the instance
    # Employee.raise_amount
    # self.raise_amount
    raise_amount = 1.04
    num_of_emps = 0 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        "return the full name of the employee"
        return (f"{self.first} {self.last}")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("test1", "user1", 50000)
emp2 = Employee("test2", "user2", 60000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print("*" * 50)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("*" * 50)

print(emp1.__dict__)
print(Employee.__dict__)
print("*" * 50)

Employee.raise_amount = 1.03
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("*" * 50)

emp1.raise_amount = 1.04
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.__dict__)
print("*" * 50)

print("Number of employees: ", Employee.num_of_emps)