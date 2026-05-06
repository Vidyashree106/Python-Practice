# types of constructors
# 1. default constructor
# 2. Userdefined constructor
# 2.1 parameterized constructor
# 2.2 Non-parameterized constructor 

# default constructor:
# Example:
class employee:
    def read(self,ename='smith',salary=9000):
        self.ename=ename
        self.salary=salary
    def details(self):
        print(f'Employee name {self.ename} and salary is {self.salary}')    
e1=employee()        # Employee name martin and salary is 9000
e1.read('martin',9000)
e1.details()

e2=employee()       # Employee name smith and salary is 9000
e2.read()
e2.details()

# -------------------------------------------------------------------------------------------------------------------------------

# parameterized constructor:
class employee:
    def __init__(self,ename,salary):
        self.ename=ename
        self.salary=salary
    def details(self):
        print(f'Employee name {self.ename} and salary is {self.salary}')
emp1=employee('martin',9000)        # Employee name martin and salary is 9000
emp2=employee('smith',8000)         # Employee name smith and salary is 8000
emp1.details()
emp2.details()

# Non-parameterized constructor:
class employee:
    def __init__(self):
        pass
    def details(self):
        print(f'Employee name {self.ename} and salary is {self.salary}')
emp1=employee()        # Employee name martin and salary is 9000
emp1.ename='martin'
emp1.salary=9000
emp1.details()

emp2=employee()        # Employee name smith and salary is 8000
emp2.ename='smith'
emp2.salary=8000
emp2.details()

# -------------------------------------------------------------------------------------------------------------------------------
