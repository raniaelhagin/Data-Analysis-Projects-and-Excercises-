# Regular method, Class methods and Static methods

""" 
- Regular methods in a class automatically take the instance as 
the first argument (self)


- class method: take the class as the first argument not the instance
(by using the decorator @classmethod before the method itself)


- Static Methods: don't pass anything automatically
we include them in a class because they have some logical connection with the class
(you should use it if you don't access the instance or the class anywhere within the function)
(@staticmethod)
"""

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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount   

    @classmethod
    def from_string(cls, emp_str):
        """used as an alternative constructor"""
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee("test1", "user1", 50000)
emp2 = Employee("test2", "user2", 60000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("*" * 50)

Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("*" * 50)

# using a class method with an instance
# doesn't make sense, but just for learning 
emp1.set_raise_amount(1.04)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("*" * 50)

emp_str_1 = "John-Doe-70000"
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
print("*" * 50)

import datetime
my_date = datetime.date(2023, 9, 5)

print(Employee.is_workday(my_date))