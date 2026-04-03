# If else condition statements
# # Syntax:
#         if condition:
#             # true statement block
#         else:
#             # false statement block

# WAP to check the given number is even or odd
num=97
if num%2==0:
    print(f'{num} is even number')
else:
    print(f'{num} is odd number')       # 97 is odd number

# WAP to check the given number is positive or negative
num1=-45
if num1>0:
    print(f'{num1} is positive')
else:
    print(f'{num1} is negative')        # -45 is negative

# WAP to check the given character is uppercase or not
ch='D'
if ch>='A' and ch<='Z':
    print(f'{ch} is uppercase')
else:
    print(f'{ch} is not uppercase')     # D is uppercase

# WAP to check the given character is lowercase or not
ch='b'
if ch>='a' and ch<='z':
    print(f'{ch} is lowercase')
else:
    print(f'{ch} is not lowercase')     # b is lowercase

# WAP check the given year is leap year or not    
year=1998
if(year%400==0) or (year%4==0 and year%100!=0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')    # 1998 is not a leap year

# WAP to check the given collection(data) is collection data or not
data=[10,20,30]
if type(data) in [list,tuple,set,dict,str]:
    print(f'{data} is collection datatype')
else:
    print(f'{data} is not collection datatype')    # [10, 20, 30] is collection datatype

# WAP to remove the duplicate elements from the given data if is collection datatype
data=[10,20,30,40,30,30]
if type(data) in [list,tuple,str,set,dict]:
    print(f'{list(set(data))} is collection datatype')
else:
    print(f'{data} is not collection datatype')      # [40, 10, 20, 30] is collection datatype

# WAP check the given value is string datatype
s1='python'
if type(s1)==str:
    print(f'{s1} is string datatype')
else:
    print(f'{s1} is not string datatype')       # python is string datatype

# WAP to check the given character is present in given string or not
ch='h'
s1='python'
if ch in s1:
    print(f'{ch} is present in string {s1}')
else:
    print(f'{ch} is not present in string {s1}')     # h is present in string python

# WAP to check the given string is palindrome or not
ch='python'
if ch==ch[::-1]:
    print(f'{ch} is a palindrome')
else:
    print(f'{ch} is not a palindrome')      # python is not a palindrome

# WAP to check the balance and deposite operation
balance=98000
deposite=1000
if deposite>0:
    balance=balance+deposite
    print(f'{deposite} is deposited to account')
    print(f'after deposite the update balance is:{balance}')
else:
    print('Amount should be more than zero')     # 1000 is deposited to account
                                                 #  after deposite the update balance is:99000

# WAP to perform withdraw operation    
balance=98000
withdraw=1000
if balance>withdraw:
    balance=balance-withdraw
    print(f'{withdraw} is debited from the account')
    print(f'after withdraw the update balance is:{balance}')
else:
    print('insufficient balance')       # after withdraw the update balance is:97000