# so the CLASS is a blueprint for creating objects/instances.
# Instance varibles contain data that is unique to each object.instance.
# def init is a special method that is called when you create a new instance.
# self is the instance of the class. which means that it refers to the instance of the class.
# self.first = first - this is an instance variable.



class Employee:

    # class variable:
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

# # I want the ablity to display the email of the employee.
# This is the method to display the full name of the employee.
# Don't forget self argument for methods its the instance.
    def fullname(self):
        return (f"{self.first} {self.last}")

    def income(self,pay):
        return (f"{self.first} {self.last} makes {self.pay}")

    # methods autmoticaly take in the instance as self
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Instance varibles/input variables
emp_1 = Employee('Jay', 'Cole', 50000)
emp_2 = Employee('Rudy', 'Slyvester', 60000)



#class.email is an attribute of the class. 

print(emp_1.email)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(emp_1.email)
# print(em_2.email)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.income(emp_1.pay))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


