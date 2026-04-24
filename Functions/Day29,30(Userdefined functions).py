# User defined functions
# Types of user defined functions
# 1) Function with no argument and no return 
def display():
    print('Function with no argument and no return')        # Function with no argument and no return
display()    

#-----------------------------------------------------------------------------------------------------------------------------#

# 2)Function with argument and no return
def add(a,b):
    print(f'sum of {a} and {b} is:{a+b}')           # sum of 100 and 75 is:175
add(100,75)    

#-----------------------------------------------------------------------------------------------------------------------------#

# 3)function witn no argument and return 
def get_num():
    return 98
print(get_num())        # 98

#----OR-----

def get_num():
    return 98
res=get_num()
print(res)              # 98

# 4)Function with argument and return
def add(a,b):
    return f'sum of {a} and {b} is:{a+b}'
print(add(100,300))             # sum of 100 and 300 is:400

#-----------------------------------------------------------------------------------------------------------------------------#

# Types of argumnet in python
# 1) positional arguments
# syntax: def function_name(p1,p2):
    # block of code
    # function_name(v1,v2)
# WAP to add two numbers using positional arguments
def add(a,b):
    print(f'sum of {a} and {b} is:{a+b}')
add(100,200)        # sum of 100 and 200 is:300

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to display the student name and age
def student(name,age):
    print(f'Student name is {name} and age is {age}')
student('smith',26)         # Student name is smith and age is 26

#-----------------------------------------------------------------------------------------------------------------------------#

# Keyword argument
def employee(ename,sal):
    print(f'Employee name is :{ename} and salary is:{sal}')
employee(ename='smith',sal='98000')         # Employee name is :smith and salary is:98000
employee(sal='78900', ename='king')         # Employee name is :king and salary is:78900

#-----------------------------------------------------------------------------------------------------------------------------#

# Default argument
def greet(name='smith'):
    print(f'Hello ! {name}')        
greet()                 # Hello ! smith
greet('king')           # Hello ! king

#-----------------------------------------------------------------------------------------------------------------------------#

# Variable length argument (*args,**kwargs)
def total(*numbers):
    print('total numbers  value is:',sum(numbers))
total(20,15,98)         # total numbers  value is: 133

#----OR----

def total(*nums):
    total=0
    for digit in nums:
        total=total+digit
    print(f'Sum of digits is:{total}')
total(10,20,30)         # Sum of digits is:60

#-----------------------------------------------------------------------------------------------------------------------------#

# keyword variable length argument(*args,**kwargs)
def details(**data):
    print(data)
details(ename='smith',age=26)       # {'ename': 'smith', 'age': 26}

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given year is leap year or not using user defined function
def leapyear(year):
    if year%4==0 and (year%400==0 or year%100!=0):
        return f'{year} is a leap year'
    else:
        return f" {year} is not a leap year"
print(leapyear(2024))           # 2024 is a leap year

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find largest among 2 numbers
def highest(a,b):
    if a>b:
        return f'{a} is largest'
    else:
        return f'{b} is largest'
print(highest(98,45))           # 98 is largest

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find largest among 3 numbers
def highest(a,b,c):
    if a>b and a>c:
        return f'{a} is largest'
    elif b>a and b>c:
        return f'{b} is largest'
    else:
        return f'{c} is largest'
print(highest(10,98,45))        # 98 is largest

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find second largest among 3 numbers
def second_largest(a,b,c):
    if(a>=b and a<=c) and (a>=c and a<=b):
        return f'{a} is second largest'
    elif(b>=a and b<=c) and (b>=c and b<=a):
        return f'{b} is second largest'
    else:
        return f'{c} is second largest'
print(second_largest(10,89,45))         # 45 is second largest

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find factorial of given number
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(factorial(5))     # 120

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find count of vowels in a string
def count_vowels(text):
    count=0
    for ch in text:
        if ch in 'AEIOUaeiou':
            count=count+1
    return count
print(count_vowels('education'))       # 5

#-----------------------------------------------------------------------------------------------------------------------------#

# write a program to find length of given string
def string_len(text):
    return len(text)
print(string_len('education'))          # 9

#----OR----

def string_len(text):
    count=0
    for ch in text:
        count=count+1
    return count
print(string_len('education'))          # 9

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find sum of numbers from given list collection
def list_sum(number):
    total=0
    for i in number:
        total=total+i
    return total
print(list_sum([1,2,3,4,5]))    # 15

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find sum of digit from given number
def sum(*numbers):
    total=0
    for i in numbers:
        total=total+i
    return total
print(sum(20,15,98))        # 133

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find sum of even numbers from given list collection
def list_sum(numbers):
    total=0
    for i in numbers:
        if i%2==0:
            total=total+i
    return total
print(list_sum([1,2,3,4,5,6,7,8]))      # 20

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find product of even digit and sum of odd digits from given collection
def li(numbers):
    total=0
    product=1
    for i in numbers:
        if i%2==0:
            product=product*i
        elif i%2==1:
            total=total+i
    print(f'product is:{product} and total is:{total}')
(li([1,2,3,4,5,6,7,8,9]))            # product is:384 and total is:25

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find sum of even numbers ,sum of odd numbers,product of odd numbers from given collection
def li(numbers):
    even_sum=0
    even_product=1
    odd_sum=0
    odd_product=1
    for num in numbers:
        if num%2==0:
            even_sum+=num
            even_product*=num
        else:
            odd_sum+=num
            odd_product*=num
    print(f'Even sum:{even_sum} and even product is:{even_product} ')      
    print(f'Odd sum:{odd_sum} and odd product is:{odd_product}')
(li([1,2,3,4,5,6,7,8,9]))              

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to reverse of a string
def rev_string(text):
    rev=''
    for ch in text:
        rev=ch+rev
    return rev
print(rev_string('python'))    # nohtyp

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given string is palindrome or not
def palindrome(text):
    rev=''
    for ch in text:
        rev=ch+rev
    if text==rev:
        print(f'{text} is palindrome')
    else:
        print(f'{text} is not a palindrome')
palindrome('eye')     # eye is palindrome

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is prime number or not
def is_prime(num):
    if num<=1:
        return 'Not a prime number'
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        return 'prime numbers'
    else:
        return 'Not a prime number'
print(is_prime(7))    # prime numbers

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is armstrong number or not
def armstrong(num):
    temp=num
    total=0
    length=len(str(num))
    while temp>0:
        digit=temp%10
        total=total+digit**digit
        temp//=10
    if total==num:
        return f'{num} is armstrong'
    else:
        return f'{num} is not armstrong'
print(armstrong(153))        # 153 is not armstrong

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find fibonacci series of n terms
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b
(fibonacci(7))      # 0 1 1 2 3 5 8 

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to reverse a number
def rev_number(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev
print(rev_number(123))    # 321

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is palindrome or not
def rev_numbers(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev
def palindrome(num):
    if num==rev_numbers(num):
        return 'palindrome'
    else:
        return 'Not a palindrome'
print(palindrome(121))      # palindrome

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is strong number or not
def strong_num(num):
    temp=num
    sum_fact=0
    while temp>0:
        digit=temp%10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        sum_fact=sum_fact +fact
        temp=temp//10
    if sum_fact==num:
        print(num,'is a strong number')
    else:
        print(num,'is not a strong number')
strong_num(145)     # 145 is a strong number

#----OR-----
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
def strong_num(num):
    temp=num
    total=0
    while temp>0:
        digit = temp%10
        total=total+factorial(digit)
        temp//=10
    if total==num:
        return f'{num} is strong number'
    else:
        return f'{num} is not a strong number'
print(strong_num(145))         # 145 is strong number   

#-----------------------------------------------------------------------------------------------------------------------------#           


