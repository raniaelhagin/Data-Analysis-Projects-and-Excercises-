# Python Object Oriented programming 

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

    def fullname(self):
        "return the full name of the employee"
        return (f"{self.first} {self.last}")


emp1 = Employee("test1", "user1", 50000)
emp2 = Employee("test2", "user2", 60000)

print(emp1)
print(emp2)
print("*" * 50)
# emp1.first = "test1"
# emp1.last = "user1"
# emp1.email = "test1.user1@company.com"
# emp1.pay = 50000


# emp2.first = "test2"
# emp2.last = "user2"
# emp2.email = "test2.user2@company.com"
# emp2.pay = 60000

print(emp1.email)
print(emp2.email)
print("*" * 50)

print(emp1.fullname())
print("*" * 50)

print(Employee.fullname(emp2))
print("*" * 50)

