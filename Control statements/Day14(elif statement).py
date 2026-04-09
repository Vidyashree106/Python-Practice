# Elif statement
# Syntax:  if condition:
            #     # true statement block(if)
            # elif condition:
            #     # true statement block
            # elif condition:
            #     # true statement block
            # else:
            #     # false statement block


# WAP to check the given number is positive,negative,zero
num=-45
if num>0:
    print(f'{num} is positive')
elif num<0:
    print(f'{num} is negative') 
else:
    print('Zero')       # -45 is negative

# WAP to check the largest of 2 numbers
a=200
b=219
if a>b:
    print(f'{a} is larger')
elif b>a:
    print(f'{b} is larger')       # 219 is larger

# WAP to check the largest of 3 numbers
a,b,c=10,34,26
if a>b and a>c:
    print(f'{a} is larger')
elif b>a and b>c:
    print(f'{b} is larger')
elif c>a and c>b:
    print(f'{c} is larger')       # 34 is larger

# WAP check smallest value among 3 digit
a=100
b=200
c=300
if a<b and a<c:
    print(f'{a} is the smallest')
elif b<a and b<c:
    print(f'{b} is the smallest')
elif c<a and c<b:
    print(f'{c} is the smallest')       # 100 is the smallest

# WAP to check the given character is uppercase / lowercase / digit / special character
ch=input('enter the character:')
if ch>='A' and ch<='Z':
    print(f'{ch} is uppercase')                 # A is uppercase
elif ch>='a' and ch<='z':
    print(f'{ch} is lowercase')                 # a is lowercase
elif ch>='0' and ch<='9':
    print(f'{ch} is a digit')                   # 1 is a digit
else:
    print(f'{ch} is a special character')       # & is a special character

# WAP  to perform ATM transactions 1.checkbalance 2.deposite 3.withdraw
balance = 98000
print('ATM TRANSACTIONS')
print('1.Check balance')
print('2.Deposite')
print('3.Withdraw')
choice=int(input('Enter your choice:'))
if choice==1:
    print(f'Bank balance is:{balance}')                         # Bank balance is:98000
elif choice==2:
    amount=int(input('Enter the deposite amount:'))
    balance=balance+amount
    print(f'{amount} is deposited to account')                  # 1000 is deposited to account
    print(f'after deposite the updated balance is:{balance}')   # after deposite the updated balance is:99000
elif choice==3:
    amount=int(input('Enter the amount to be withdraw:'))
    balance=balance-amount
    print(f'{amount} has been debited from account')            # 25900 has been debited from account
    print(f'after withdraw the updated balance is:{balance}')   # after withdraw the updated balance is:72100    
else:
    print('Invalid choice')                                     # Invalid choice

# WAP to perform Arithemetic operations
print('Arithemetic calculator')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Floor division')
print('6.Modulus')
print('7.Exponent')
choice=int(input('Enter your choice:'))
a=int(input('Enter the value of a:'))    
b=int(input('Enter the value of b:'))
if choice==1:
    Sum=a+b
    print(f'Addition of a and b is:{Sum}')      # Addition of a and b is:50
elif choice==2:
    difference=a-b
    print(f'Subtraction of a and b is:{difference}')        # Subtraction of a and b is:490
elif choice==3:    
    product=a*b
    print(f'Multiplication of a and b is:{product}')        # Multiplication of a and b is:120
elif choice==4:
    division=a/b
    print(f'Division of a and b is:{division}')         # Division of a and b is:4.0
elif choice==5:
    fd=a//b
    print(f'Floor division of a and b is:{fd}')         # Floor division of a and b is:18
elif choice==6:
    mod=a%b
    print(f'Modulus of a and b is:{mod}')               # Modulus of a and b is:1
elif choice==7:
    power=a**b
    print(f'Exponent of a and b is:{power}')        # Exponent of a and b is:8
else:
    choice>=7
    print('Invalid choice')                  # Invalid choice      







