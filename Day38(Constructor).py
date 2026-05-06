# constructor function is same as --init-- function
# syntax : class class_name:
            #     class Variable
            #     def --init--(self,var1,var2,.......)
            #     self.var1 = var1/arg1
            #     self.var2 = var2/agr2
            # object=class_name(val1,val2,....)
            # print(object.val1,object.val2,.....)

# Programming example
class employee:
    def __init__(self,ename,eid,sal,location,job):
        self.ename=ename
        self.eid=eid
        self.sal=sal
        self.location=location
        self.job=job
emp1=employee('smith','E01',98000,'Bangalore','Analyst')        # creating object outside the class
print(f'Employee name is: {emp1.ename}')            # Employee name is: smith
print(f'Employee id is:{emp1.eid}')                 # Employee id is:E01
print(f'Employee salary is:{emp1.sal}')             # Employee salary is:98000
print(f'Employee location is:{emp1.location}')      # Employee location is:Bangalore
print(f'Location is:{emp1.job}')                    # Location is:Analyst

# ------------------------------------------------------------------------------------------------------------------------------- 

# WAP to create class employee => name,salary,department use the init method to initialise this values when an object is created 
# add a method display details of to print create 2 object and display their details
class employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
   
    def display(self):                              # method
        print(f'Name:{self.name}')                   # Name:King
        print(f'Salary:{self.salary}')               # Salary:98000
        print(f'Department:{self.department}')       # Department:Research

emp=employee('King',98000,'Research')
emp.display()

emp1=employee('Smith',95000,'Analysis')
emp1.display()

# -------------------------------------------------------------------------------------------------------------------------------

# WAP to create class person to display name and age
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'person name:{self.name}')
        print(f'person age:{self.age}')
p1=person('smith',26)                       # person name:smith
p1.display()                                # person age:26
print()
p2=person('king',28)                        # person name:king
p2.display()                                # person age:28

#-------------------------------------------------------------------------------------------------------------------------------

# WAP to display bank name,customer name and account balance using constructor method
class bank_account:
    bank_name='icici'
    def __init__(self,cname,balance):
        self.cname=cname
        self.balance=balance
    def details(self):
        print(f'customer name:{self.cname}')                # customer name:scott
        print(f'balance is:{self.balance}')                 # balance is:9800
        print(f'bankname is:{bank_account.bank_name}')      # bankname is:icici
c1=bank_account('scott',9800)
c1.details()

#-------------------------------------------------------------------------------------------------------------------------------

# WAP to display multiple customer information by taking user input
class BankAccount:
    bank_name = 'Icici Bank'     # class variable
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_content(self):
        print(f'Account holder: {self.account_holder}')
        print(f'Balance is: {self.balance}')

num = int(input('Enter the number of accounts to be added: '))
accounts = []

for i in range(num):
    print(f'\nEnter details of account {i+1}')      # Enter details of account 1
    name = input('Enter the name: ')                # Enter the name: vidya
    balance = int(input('Enter the balance: '))     # Enter the balance: 50000
    acc = BankAccount(name, balance)
    accounts.append(acc)
    
print('\nAccount details:')
for acc in accounts:                                # Account holder: vidya
    acc.display_content()                           # Balance is: 50000  

#-------------------------------------------------------------------------------------------------------------------------------

# WAP for ATM scenario using constructor method
class BankName:

    def _init_(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_pin(self):
        try:
            enter_pin = int(input('Enter the pin: '))
            if enter_pin != self.pin:
                raise ValueError('Incorrect pin')
            return True
        except ValueError as e:
            print('error:', e)
            return False

    def deposit(self):
        if self.check_pin():
            amount = int(input('Enter the amount to deposit: '))
            if amount > 0:
                self.balance = self.balance + amount
                print(f'{amount} has been deposited')
                print(f'after deposit balance: {self.balance}')
            else:
                print('Enter valid amount')

    def withdraw(self):
        if self.check_pin():
            amount = int(input('Enter the amount to withdraw: '))
            if amount < self.balance:
                self.balance = self.balance - amount
                print(f'{amount} has been debited')
                print(f'after withdraw balance: {self.balance}')
            else:
                print('Enter valid amount')

    def display(self):
        if self.check_pin():
            print(f'bank balance is: {self.balance}')

acct = BankName('Smith', 1234, 97000)
acct.deposit()
acct.withdraw()
acct.display()

#-------------------------------------------------------------------------------------------------------------------------------






    


