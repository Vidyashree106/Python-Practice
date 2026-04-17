# Functions
# types-> 1) Built-in function       2) User defined function
# 1) Built-in funtion

# String methods in python:
# Syntax: print(dir(str))  // to find string methods
# Syntax : variablename.methodname() // to perform operation using string methods 

# capitalize method:
msg='welcome to python class'
print(msg.capitalize())         # Welcome to python class    

#--------------------------------------------------------------------------------------------------------------------------------------#

# upper method:
msg='python'
print(msg.upper())      # PYTHON

#------OR-------
msg='python'
result=msg.upper()
print('result')         # # PYTHON

#--------------------------------------------------------------------------------------------------------------------------------------#

# lower method:
msg="JAVA"
print(msg.lower())      # java

#--------------------------------------------------------------------------------------------------------------------------------------#

# Swap case: upper to lower & lower to upper
msg='PythOn'
print(msg.swapcase())     # pYTHoN

#--------------------------------------------------------------------------------------------------------------------------------------#

# count method:
# Syntax: variablename,count(substring)
msg='pyspiders'
print(msg.count('s'))     # s

msg='pyspiders'
print(msg.count('j'))       # 0

msg='pyspiders'
print(msg.count('r'))       # 1

string='welcome to python class'
print(string.count('python'))       # 1

#--------------------------------------------------------------------------------------------------------------------------------------#

# Index method
msg='welcome to python class'
first=msg.index('o')
print(first)        # 4

# WAP to find position of second occurance character 
msg='welcome to python class'
first=msg.index('o')
second=msg.index('o',first+1)
print(second)       # 9

# WAP to find position of third occurance character 
msg='welcome to python class'
first=msg.index('o')
second=msg.index('o',first+1)
third=msg.index('o',second+1)
print(third)        # 15

# WAP to find position of third occurance character using enumerate function
msg='welcome to python class'
count=0
for i,ch in enumerate(msg):
    if ch=='o':
        count=count+1
        if count==3:
            print(i)            # 15
            break

#--------------------------------------------------------------------------------------------------------------------------------------#

# find method
# Syntx: variablename.find(sunstring)
string='pyspiders'        
print(string.find('s'))    # 2    

string='pyspiders'  
print(string.find('j'))     # -1

#--------------------------------------------------------------------------------------------------------------------------------------#

# r-index method
msg='python python'
print(msg.rindex('n'))      # 12

#--------------------------------------------------------------------------------------------------------------------------------------#

# replace method
msg='python'
print(msg.replace('t','*'))     # py*hon

#--------------------------------------------------------------------------------------------------------------------------------------#

# Startswith method
# Syntax: variablename.startswith('substr')
msg='education'
print(msg.startswith('e'))      # True
print(msg.startswith('a'))      # False
print(msg.startswith('A'))      # False

#--------------------------------------------------------------------------------------------------------------------------------------#

# Endswith method
# Syntax: variablename.endswith('substr')
msg='python'
print(msg.endswith('n'))        # True
print(msg.endswith('a'))        # False
print(msg.endswith('p'))        # False

#--------------------------------------------------------------------------------------------------------------------------------------#

# split method
# syntax: variablename.split()
string='welcome to python class'
print(string.split())
print(string.split('o'))

#--------------------------------------------------------------------------------------------------------------------------------------#

# strip method
# syntax: variablename.strip()
string=' python '
print(string.strip())       # python

#--------------------------------------------------------------------------------------------------------------------------------------#

# rstrip method
# syntax: variablename.rstrip()
msg=' python '
print(msg.rstrip())         #  python

#--------------------------------------------------------------------------------------------------------------------------------------#

# lstrip method
# syntax: variablename.lstrip()
msg=' python '
print(msg.lstrip())         # python

#--------------------------------------------------------------------------------------------------------------------------------------#

# join method
# syntax: separator.join(iterable)
words='education'
print('*'.join(words))      # e*d*u*c*a*t*i*o*n

li=['10','45','78']
print('$'.join(li))         # 10$45$78

li=['smith','king']
print('%'.join(li))         # smith%king

#--------------------------------------------------------------------------------------------------------------------------------------#

# isalpha method
# syntax: variablename.isalpha()
s='python'
print(s.isalpha())      # True

s='python1213'
print(s.isalpha())      # False

#--------------------------------------------------------------------------------------------------------------------------------------#

# isalnum method
# syntax: variablename.isalnum()
s='135465465'
print(s.isalnum())      # True

s='python767'
print(s.isalnum())      # true

#--------------------------------------------------------------------------------------------------------------------------------------#

# islower method
# syntax: variablename.islower()
s='python'
print(s.islower())       # True 

s='PyThoN'
print(s.islower())      # False

#--------------------------------------------------------------------------------------------------------------------------------------#

# isupper method
# syntax: variablename.isupper()
s='PYTHON'
print(s.isupper())          # True

s='pythOn'
print(s.isupper())          # False

#--------------------------------------------------------------------------------------------------------------------------------------#

# isdigit method
# syntax: variablename.isdigit()
num='123456'
print(num.isdigit())        # True

s='python1234'
print(s.isdigit())          # False

#--------------------------------------------------------------------------------------------------------------------------------------#

# zfill method
# syntax: string.zfill(length)
('smith'.zfill(9))          # '0000smith'

#--------------------------------------------------------------------------------------------------------------------------------------#

# WAP to print extension of the file name
file='pyspiders.com'
result=file.split('.')
print(result[-1])           # com

#--------------------------------------------------------------------------------------------------------------------------------------#

# isinstance method
# syntax : isinstance(object,type)
a=98
print(isinstance(a,int))            # True

b='smith'
print(isinstance(b,str))            # true

b='smith'
print(isinstance(b,int))            # False
#--------------------------------------------------------------------------------------------------------------------------------------#

# WAP to calculate uppercase and lowercase letters from given string
s='python'
upper=0
lower=0
for ch in s:
    if ch.isupper():
        upper=upper+1
    elif ch.islower():
        lower=lower+1
print(f'count of uppercase:{upper}')        # count of uppercase:0
print(f'count of lowercase:{lower}')        # count of lowercase:6

#--------------------------------------------------------------------------------------------------------------------------------------#
