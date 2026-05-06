# Creating class and object
# syntax for creating class and object:
# class className:
#     properties(variables)
#     methods(function)
# object=className

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to create class and object using class variables
class student:
    sname='smith'       # class variable
    age=26               # class variable
    subject='Python'     # class variable
obj=student()
print(f'student name is:{obj.sname}')           # student name is:smith
print(f'Student age is:{obj.age}')              # Student age is:26
print(f'Student subject is:{obj.subject}')      # Student subject is:Python

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to display multiple object information using object variables
class employee:
    pass
emp1=employee()
emp1.ename='smith'
emp1.salary=98000
emp2=employee()
emp2.ename='john'
emp2.salary=76655
print(f'Employee 1 name:{emp1.ename} and salary is:{emp1.salary}')
print(f'Employee 2 name:{emp2.ename} and salary is:{emp2.salary}')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to display multiple object information
class car:
    pass
# create mini cooper car object
car1=car()
car1.model='s'
car1.year=2021
car1.color='white'
car1.milage=20

# create BMW car object
car2=car()
car2.model='M3'
car2.year=2023
car2.color='Black'
car2.milage=30

# display the informtaion
print('car1:Mini Cooper')
print('model:',car1.model)
print('year:',car1.year)
print('color:',car1.color)
print('milage',car1.milage)

print('car2:BMW')
print('model:',car2.model)
print('year:',car2.year)
print('color:',car2.color)
print('milage',car2.milage)

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to create class variable and object variable
class Employee:
    company_name='pyspiders'        # class variable
    location='Bangalore'            # class variable

emp1=Employee()
emp1.ename='smith'                  # object variable
emp1.sal=98000                      # object variable

emp2=Employee()
emp2.ename='scott'                  # object variable
emp2.sal=76000                      # object variable

print(f'Employee1 name is:{emp1.ename} and salary is:{emp1.sal}')
print(f'Employee2 name is:{emp2.ename} and salary is:{emp2.sal}')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to access the class variable without creating object
class student:
    sname='martin'
    age=26
    subject='python'
    def display():
        print(f'Student name is:{student.sname}')
        print(f'Student age is:{student.age}')
        print(f'Student subject is:{student.subject}')
student.display()

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to access class variable using function inside the class but by creating object
class student:
    sname='martin'
    age=26
    subject='python'
    def display(self):
        print(f'Student name is:{student.sname}')
        print(f'Student age is:{student.age}')
        print(f'Student subject is:{student.subject}')
s1=student()
s1.display()

# self is used to access varaible and method present inside the class

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to display employee information using function inside class by creating object
class Employee:
    sname='king'
    age=26
    subject='python'
    DOJ='20-10-2002'
    def display(self):
        print(f'Student name is:{Employee.sname}')
        print(f'Student age is:{Employee.age}')
        print(f'Student subject is:{Employee.subject}')
        print(f'DOJ is:{Employee.DOJ}')    
e=Employee()
e.display()    

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to display employee name,salary and amount slaray by using function inside the class and by creating object
class Employee:
    ename='smith'
    salary=5000
    def details(self):
        print(f'employee name:{self.ename}')
        print(f'employee salary:{self.salary}')
        print(f'employee annual slaray:{self.salary*12}')
emp=Employee()
emp.details()

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to display multiple object information using function as an object
class Employee:
    dname='analysis'
    def details(self,ename,sal,job):
        self.ename=ename
        self.sal=sal
        self.job=job
    def display(self):
        print(f'employee name:{self.ename}')
        print(f'employee salary:{self.sal}')
        print(f'employee job:{self.job}') 
        print(f'employee department:{Employee.dname}')
e1=Employee()
e1.details('smith',800,'clerk')
e1.display()
print()
e2=Employee()
e2.details('king',900,'analyst')
e2.display()

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP class variable->bank_name     instance variable->cxname,balance       methods->details(),deposite(),withdraw(),display()
class Bank:
    bank_name='State bank of India'
    def details(self,cxname,balance):
        self.cxname=cxname
        self.balance=balance
    def deposite(self,amount):
        self.balance=self.balance+amount
        print(f'Amount deposited:{amount}')
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f'Amount withdrawn:{amount}')
        else:
            print(f'Insufficient balance')
    def display(self):
        print(f'Bank name :{self.bank_name}')
        print(f'Customr name :{self.cxname}')
        print(f'Account balance :{self.balance}')
# customers
c1=Bank()
c1.details('smith',5000)
c1.deposite(10000)
c1.withdraw(8000)
c1.display()
print()
c2=Bank()
c2.details('king',10000)
c2.deposite(1000)
c2.withdraw(500)
c2.display()

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP an ATM program using class and object withdraw using constructor method and implement check balance,
# deposite and withdraw with exception handling
class ATM:

    def set_balance(self, amount):
        self.balance = amount

    def check_balance(self):
        print(f'Current Balance: {self.balance}')

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError('Deposit amount must be positive')
            self.balance += amount
            print(f'{amount} deposited successfully')
            print(f'Updated balance: {self.balance}')
        except ValueError as e:
            print('Error:', e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError('Withdrawal amount must be positive')
            if amount > self.balance:
                raise Exception('Insufficient balance')
            self.balance -= amount
            print(f'{amount} withdrawn successfully')
            print(f'Remaining balance: {self.balance}')
        except ValueError as e:
            print('Error:', e)
        except Exception as e:
            print('Error:', e)

# Creating object
user1 = ATM()
# Setting initial balance
user1.set_balance(1000)
# Menu driven program
while True:
    print('\n--- ATM Menu ---')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        user1.check_balance()
    elif choice == '2':
        try:
            amount = float(input('Enter amount to deposit: '))
            user1.deposit(amount)
        except ValueError:
            print('Invalid input! Please enter a number.')
    elif choice == '3':
        try:
            amount = float(input('Enter amount to withdraw: '))
            user1.withdraw(amount)
        except ValueError:
            print('Invalid input! Please enter a number.')
    elif choice == '4':
        print('Thank you for using ATM!')
        break
    else:
        print('Invalid choice! Please try again.')

#-----------------------------------------------------------------------------------------------------------------------------#
