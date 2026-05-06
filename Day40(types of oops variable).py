# Types of variables in object oriented programming
# 1. Instance variable      #(object level variables)
# 2. Static variable        #(class level variables)
# 3. Local variable

# 1. Instance variable: It is a variable that is defined inside a class and is associated with an instance of the class. 
# Each instance of the class has its own copy of the instance variable. It is accessed using the self keyword.

# WAP to create instance variables
class Employee:
    def __init__(self,ename,job):
        self.ename=ename
        self.job=job
    
    def display(self):
        print(f'Employee name is {self.ename} and job is {self.job}')
emp=Employee('smith','analyst')
emp.display()

# -------------------------------------------------------------------------------------------------------------------------------

# 2. Static variable: It is a variable that is defined inside a class but outside any method. 
# It is shared by all instances of the class. 
# It is accessed using the class name.

# Example of static variable
class Employee:
    company_name='Techcrop'     # static class variables shared by all employees

    def __init__(self,ename,job):
        self.ename=ename
        self.job=job

    def display(self):
        print(f'Employee name is {self.ename} and job is {self.job} and company name is {Employee.company_name}')

# creating employee objects
emp1=Employee('smith','SQL developer')
emp2=Employee('john','python developer')
emp1.display()
emp2.display()

# -------------------------------------------------------------------------------------------------------------------------------

# 3. Local variable: It is a variable that is defined inside a method and is only accessible within that method.
# Example of local variable
class Employee:
    def __init__(self,ename,monthly_salary,job):
        self.ename=ename
        self.monthly_salary=monthly_salary
        self.job=job

    def calculate_annual_salary(self):
        annual_salary=self.monthly_salary*12        # local variable that is only accessible within this method
        print(f'Employee name is {self.ename} and job is {self.job} ')      # Employee name is smith and job is SQL developer 
        print(f'Annual salary is {annual_salary}')                          # Annual salary is 60000

# create employee object
emp=Employee('smith',5000,'SQL developer')

# calculate and display annual salary
emp.calculate_annual_salary()

# -------------------------------------------------------------------------------------------------------------------------------

# Example 2 for local variable
class student:
    def details(self):
        sname='smith'
        age=26
        print(f'Student name is {sname} and age is {age}')      # Student name is smith and age is 26
s1=student()
s1.details()

# -------------------------------------------------------------------------------------------------------------------------------

# WAP to check the given number is palindrome or armstrong or strong number
class Numbers:
    def palindrome(self,num):
        rev=str(num)[::-1]
        if str(num)==rev:
            print(f'{num} is a palindrome')
        else:
            print(f'{num} is not a plaindrome')

    def armstrong(self,num):
        length=len(str(num))
        cube=0
        for i in str(num):
            cube=cube+int(i)**length
        if cube==num:
            print(f'{num} is armstrong')
        else:
            print(f'{num} is not a armstrong number')

    def strong(self,num):
        sum=0
        for digit in str(num):
            fact=1
            for i in range(1,int(digit)+1):
                fact=fact*i
            sum=sum+fact
        if sum==num:
            print(f'{num} is strong number')
        else:
            print(f'{num} is not a strong number')

obj=Numbers()
obj.palindrome(145)
obj.armstrong(153)
obj.strong(145)

# -------------------------------------------------------------------------------------------------------------------------------
