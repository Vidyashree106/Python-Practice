# While loop is used to execute a block of code repeatedly as long as a certain condition is true.
# Syntax:
    #  initialisation
    #     while condition:
    #         # statement block
    #         # block of code
    #     updation
    # else:
    #     # statement

# WAP to print natural number from 1 to 5
i=1
while i<=5:
    print(i ,  end=' ')
    i=i+1
else:
    print('Program completed')      # 1 2 3 4 5 Program completed

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print number 5 to 1
i=5
while i>=1:
    print(i, end=" ")    
    i=i-1
else:
    print('Program completed')      # 5 4 3 2 1 Program completed

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print natural numbers  from 1 to 5
i=1
while i<=5:
    print(i, end=" ")
    i=i+1
else:
    print('Program completed')      # 1 2 3 4 5 Program completed

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print number 5 to 1
i=5
while i>=1:
    print(i, end=" ")    
    i=i-1
else:
    print('Program completed')      # 5 4 3 2 1 Program completed

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print even digit number from 1 to 10
i=2
while i<=10:
    if i%2==0:
        print(i, end=" ")
    i=i+1                           # 2 4 6 8 10 

# OR
i=2 
while i<=10:
    print(i, end=" ")
    i=i+2                       # 2 4 6 8 10

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print odd digit number from 1 to 10
i=1
while i<=10:
    if i%2==1:
        print(i, end=" ")
    i=i+1                           # 1 3 5 7 9    

# OR
i=1
while i<=10:
    print(i, end=" ")
    i=i+2                       # 1 3 5 7 9

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print hello python 3 times
i=1
while i<=3:
    print("Hello Python", end=" ")
    i=i+1                       # Hello Python Hello Python Hello Python    

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print tables of given number
num=2
i=1
while i<=10:
    print(f'{num} * {i} = {num*i}')          # 2 * 1 = 2
    #                                         2 * 2 = 4
    #                                         2 * 3 = 6
    #                                         2 * 4 = 8
    #                                         2 * 5 = 10
    #                                         2 * 6 = 12
    #                                         2 * 7 = 14
    #                                         2 * 8 = 16
    #                                         2 * 9 = 18
    #                                         2 * 10 = 20
    i=i+1
     
#----------------------------------------------------------------------------------------------------------------------------#     

# WAP to print sum of 5 natural numbers
i=1
total=0
while i<=5:
    total=total+i
    i=i+1
print(f'Sum of 5 natural numbers is {total}')     # Sum of 5 natural numbers is 15

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find sum of even digit number from 1 to 20
i=2
total=0
while i<=20:
    if i%2==0:
        total=total+i
    i=i+2
print(f'Sum of even digit number from 1 to 20 is {total}')     # Sum of even digit number from 1 to 20 is 110

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find number of digits present in given number
num=43879
count=0
while num>0:
    count=count+1
    num=num//10
print(count)        #  5

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print elements of list are even number or odd number
list=[23,44,45,98,39]
i=0
while i<len(list):
    if list[i]%2==0:
        print(f'{list[i]} is even number')
    else:
        print(f'{list[i]} is odd number')
    i=i+1  
# 23 is odd number     
# 44 is even number    
# 45 is odd number     
# 98 is even number    
# 39 is odd number            

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print the number which are divisible by 3 from 1 TO 10
n=1
while n<=10:
    if n%3==0:
        print(f'{n} is divisible by 3')
    n=n+1
# 3 is divisible by 3
# 6 is divisible by 3
# 9 is divisible by 3

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print number which are divisible by 3 and 5 from 1 to 10
n=1
while n<=10:
    if n%3==0 and n%5==0:
        print(f'{n} is divisible by 3 and 5')
    else:
        print(f'{n} is not divisible by 3 and 5')
    n=n+1
# 1 is not divisible by 3 and 5
# 2 is not divisible by 3 and 5
# 3 is not divisible by 3 and 5
# 4 is not divisible by 3 and 5
# 5 is not divisible by 3 and 5
# 6 is not divisible by 3 and 5
# 7 is not divisible by 3 and 5
# 8 is not divisible by 3 and 5
# 9 is not divisible by 3 and 5
# 10 is not divisible by 3 and 5

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print number whose last digit is present between 6 to 9 from 25 to 30
num=25
while num<=30:
    last_digit=num%10
    if last_digit>=6 and last_digit<=9:
        print(num)
    num=num+1
# 26
# 27
# 28
# 29 

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print even digit from the given number
num=5845
while num>0:
    digit=num%10
    if digit%2==0:
        print(f'{digit} is an even number')
    num=num//10
# 4 is an even number
# 8 is an even number

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print even digit from given number if digit is greater than 4
num=543879
while num>0:
    digit=num%10
    if digit%2==0 and digit>4:
        print(f'{digit} is an even number and greater than 4')
    num=num//10
# 8 is an even number and greater than 4

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print digit which are greater than 4 from given number
num=16489
while num>0:
    digit=num%10
    if digit>4:
        print(digit,end=' ')
    num=num//10     # 6 8 9 

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the sum of all digits from given number
num=16489
total=0
while num>0:
    digit=num%10
    total=total+digit
    num=num//10
print(total)    # 28

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print sum of even digits from given number
num=16489
total=0
while num>0:
    digit=num%10
    if digit%2==0:
        total=total+digit
    num=num//10
print(f'Sum of even numbers is:{total}')   
# Sum of even numbers is:18

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the product of digits from given number
num=354
product=1
while num>0:
    digit=num%10
    product=product*digit
    num=num//10
print(f'Product of digits is:{product}')   # Product of digits is:60

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find sum of all digits and product of all digits from given number
num=354
total=0
product=1
while num>0:
    digit=num%10
    total=total+digit
    product=product*digit
    num=num//10
print(f'Sum of digits is:{total}')        # Sum of digits is:12
print(f'Product of digits is:{product}')   # Product of digits is:60

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find sum of even digits and product of odd digits from given number
num=8547
total=0
product=1
while num>0:
    digit=num%10
    if digit%2==0:
        total=total+digit
    else:
        product=product*digit
    num=num//10
print(f'sum of even numbers is:{total}')        # sum of even numbers is:12
print(f'product of odd numbers is:{product}')       # product of odd numbers is:35

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print sum and product of even number and odd number
num=8547
even_total=0
odd_total=0
even_product=1
odd_product=1
while num>0:
    digit=num%10
    if digit% 2==0:
        even_total=even_total+digit
        even_product=even_product*digit
    elif digit%2==1:
        odd_total=odd_total+digit
        odd_product=odd_product*digit
    num=num//10
print(f'Sum of even number is:{even_total}')            # Sum of even number is:12
print(f'Product of even number is:{even_product}')      # Product of even number is:32
print(f'Sum of odd number is:{odd_total}')              # Sum of odd number is:12
print(f'Product of odd number is:{odd_product}')        # Product of odd number is:35

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to revers a given number
num=794
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(f'Reverse of a given number is:{rev}')    # Reverse of a given number is:497

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is palindrome or not
num=797
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev:
    print(f'{num} is a palindrome')     # 797 is a palindrome
else:
    print(f'{num} is not a palindrome')    

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print highest digit from given number
num=598
highest=float('-inf')
while num>0:
    digit=num%10
    if digit>highest:
        highest=digit
    num=num//10
print(f'Highest digit is:{highest}')        # Highest digit is:9

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print lowest digit from the given number
num=598
lowest=float('inf')
while num>0:
    digit=num%10
    if digit<lowest:
        lowest=digit
    num=num//10
print(f'Lowest digit is :{lowest}')        # Lowest digit is :5

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the highest value from the list collection
list=[3,7,9,2]
highest=float('-inf')
i=0
while i<len(list):
    if list[i]>highest:
        highest=list[i]
    i=i+1
print(f'Highest value is:{highest}')       # Highest value is:9

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the second largest from the given digit
num=4981
largest=float('-inf')
second_largest=float('-inf')
while num>0:
    digit=num%10
    if digit>largest:
        second_largest=largest
        largest=digit
    elif digit>second_largest and digit!=largest:
        second_largest=digit
    num=num//10
print(f'Second largest is :{second_largest}')        # Second largest is :8

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the second largest from the given collection
list=[4,9,2]    
i=0
largest=float('-inf')
second_largest=float('-inf')
while i<len(list):
    if list[i]>largest:
        second_largest=largest
        largest=list[i]
    elif list[i]>second_largest and list[i]!=largest:
        second_largest=list[i]
    i=i+1
print(f'Second largest from the collection is:{second_largest}')          # Second largest from the collection is:4    

#----------------------------------------------------------------------------------------------------------------------------#

# WAP toncheck the given number is prime number or not
num=7                   
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(f'{num} is a prime number')     # 7 is a prime number
else:
    print(f'{num} is not a prime number')   

# OR
num=4
i=2    
count=0
while i < num:
    if num % i==0:
        count=count+1
    i=i+1
if count==0 and num>1:
    print(f'{num} is a prime number')       # 5 is a prime number
else:
    print(f'{num} is not a prime number')       # 4 is not a prime number

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print prime numbers from 1 to 30
num=1
while num<=30:
    i=1
    count=0
    while i<=num:
        if num%i==0:
            count=count+1
        i=i+1
    if count==2:
        print(num ,end=' ') 
    num=num+1                   # 2 3 5 7 11 13 17 19 23 29

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is armstrong number or not 
num=153
temp=num
sum_cubes=0
length=len(str(num))
while num > 0:
    digit = num % 10
    sum_cubes=sum_cubes+digit**length
    num=num//10
if temp == sum_cubes:
        print(f'{temp} is armstrong number')        # 153 is armstrong number
else:
        print(f'{temp} is not armstrong number')

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print armstrong number from 1 to 1000
num=1
while num<=10000:
    temp=num
    sum_cubes=0
    length=len(str(num))
    while temp > 0:
        digit = temp % 10
        sum_cubes=sum_cubes+digit**length
        temp=temp//10
    if num == sum_cubes:
        print(num, end=' ')        # 1 2 3 4 5 6 7 8 9 153 370 371 407 1634 8208 9474 
    num=num+1                   

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print fibonacci series up to n terms
n=5
a,b=0,1
count=0
while count<n:
    print(a, end=' ')
    temp=a+b
    a=b
    b=temp
    count=count+1  # 0 1 1 2 3

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is Neon number or not
num=9
square=num**2
sum_digits=0
temp=square
while temp>0:
    digit=temp%10
    sum_digits=sum_digits+digit
    temp=temp//10
if sum_digits==num:
    print(f'{num} is a neon number')     # 9 is a neon number   
else:    
    print(f'{num} is not a neon number')    

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print neon number from 1 to 1000
num=1
while num<=1000:
    square=num**2
    sum_digits=0
    temp=square
    while temp>0:
        digit=temp%10
        sum_digits=sum_digits+digit
        temp=temp//10
    if sum_digits==num:
        print(num, end=' ')     # 1 9 
    num=num+1 

#----------------------------------------------------------------------------------------------------------------------------#
    
# WAP to print sum of all the elements from given list colection    
li=[1,2,3,4,5,6,7]
i=0
total=0
while i<len(li):
    total=total+li[1]
    i=i+1
print(f'Sum of list collection is:{total}')         # Sum of list collection is:14

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find factorial of an number
num=5
temp=num
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(f'fact of {temp} is:{fact}')              # fact of 5 is:120

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to print ASCII value of each character from given string
s='python'
i=0
while i<len(s):
    print(s[i],':',ord(s[i]))
    i=i+1
# p : 112
# y : 121
# t : 116
# h : 104
# o : 111
# n : 110

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to convert string to upper case
s='python'
i=0
res=''
while i<len(s):
    res=res+chr(ord(s[i])-32)
    i=i+1
print(f'the upper case of given string is:{res}')      # the upper case of given string is:PYTHON

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to convert string to lower case
s='PYTHON'
i=0
res=''
while i<len(s):
    res=res+chr(ord(s[i])+32)
    i=i+1
print(res)          # python

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to toggle character
s='PythON'
i=0
res=''
while i<len(s):
    if s[i]>='A' and s[i]<='Z':
        res=res+chr(ord(s[i])+32)
    elif s[i]>='a' and s[i]<='z':
        res=res+chr(ord(s[i])-32)
    i=i+1
print(res)    # pYTHon

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find number of character present in given string
s='python'
i=0
count=0
while i<len(s):
    count=count+1
    i=i+1
print(f'Total no of character present in given {s} is:{count}')    # Total no of character present in given python is:6

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the occurance of particular character in given string
s='Qspidersss'
ch='s'
count=0
i=0
while i<len(s):
    if ch==s[i]:
        count=count+1
    i=i+1
print(count)            # 4

#----------------------------------------------------------------------------------------------------------------------------#

# WAP count of vowels present in string
s='Apple'
count=0
i=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        count=count+1
    i=i+1
print(count)        # 2

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find count of vowels and consonanths in given string
s='education'
i=0
vowels=0
cons=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        vowels=vowels+1
    elif s[i] not in 'AEIOUaeiou':
        cons=cons+1
    i=i+1
print(f'vowels are:{vowels}')       # vowels are:5
print(f'consonants are:{cons}')       # consonants are:4

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to find count of vowels and consonanths in given string and digits
s='education123456'
i=0
vowels=0
cons=0
digit=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        vowels=vowels+1
    elif s[i]>='0' and s[i]<='9':
        digit=digit+1    
    elif s[i] not in 'AEIOUaeiou':
        cons=cons+1
    i=i+1    
print(f'vowels are:{vowels}')       # vowels are:5
print(f'consonants are:{cons}')     # consonants are:4
print(f'digits are:{digit}')       # digits are:6

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to check username and password if user is entering wrong username and password if entering wrong username and password 
#it should display invalid credentials, if user is entering invalid credentials more than 3 times display account blocked
username='scott'
password='tiger'
i=0
while i<3:
    user=input('Enter username:')
    pwd=input('Enter password:')
    if user==username and pwd==password:
        print('Login successful')
        break
    else:
        print('Invalid credentials')
    i=i+1
else:    print('Account blocked')

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to build ATM project for pin authentication,check balance,withdraw money,deposit money 
pin='1234'
balance=1000.00
attemps=0
# PIN authentication
while attemps<3:
    entered_pin=input('Enter your PIN:')
    if entered_pin==pin:
        print('login successfull')
        break
    else:
        print('Invalid PIN')
        attemps=attemps+1
else:
    print('Account blocked')
    exit()

# Check balance, withdraw money, deposit money
while True:
    print("\n 1.Balance \n 2.Deposit \n 3.Withdraw \n 4.Exit")
    choice=input('choose:')
    if choice=='1':
        print(f'Your balance is:{balance}')
    elif choice=='2':
        amount=float(input('Deposit:'))
        balance=balance+amount
        print(f'Your new balance is:{balance}')
    elif choice=='3':
        amount=float(input('Withdraw:'))
        if amount<=balance:
         balance=balance-amount
         print(f'Your new balance is:{balance}')
        else:
            print('Insufficient balance')
    elif choice=='4':
        print('Goodbye!')
        break
    else:
        print('Invalid choice')

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is strong number or not
num=145
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
if temp==sum:
    print(f'{temp} is a strong number')     # 145 is a strong number
else:    
    print(f'{temp} is not a strong number')

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is perfect number or not
num=6
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print(f'{num} is a perfect number')     # 6 is a perfect number
else:    
    print(f'{num} is not a perfect number')

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is spy number or not
n=1124
temp=n
sum=0
product=1
while n>0:
    digit=n%10
    sum=sum+digit
    product=product*digit
    n=n//10
if sum==product:
    print(f'{temp} is a spy number')     # 1124 is a spy number
else:    
    print(f'{temp} is not a spy number')

#----------------------------------------------------------------------------------------------------------------------------#

# WAP to book ticket in book my show application first it should ask theater name and then it should display the moveis available 
# then it has to display ticket price it should ask confirmation to book ticket
print('Welcome to BookMyShow!')
while True:
    theater_name=input('Enter theater name(PVR,INOX)or type "exit" to quit:')
    if theater_name.lower()=='exit':
        print('Thank you for using BookMyShow!')
        break
    if theater_name in ['PVR','INOX']:  
        if theater_name=='PVR':
            print('Movies available at PVR:')
            movie1='Avathar: The Way of Water'
            movie2='The Batman'
            ticket_price1=900
            ticket_price2=800
        else:
            theater_name=='INOX'
            print('Movies available at INOX:')
            movie1='Mission Impossible:fallout'
            movie2='Jurassic World: Dominion'
            ticket_price1=850
            ticket_price2=750
        print(f'1.{movie1}')
        print(f'2.{movie2}')
        movie_choice=input('Choose a movie (1 or 2):')
        if movie_choice=='1' or movie_choice=='2':
            if movie_choice=='1':
                selected_movie=movie1
                ticket_price=ticket_price1
            else:
                selected_movie=movie2
                ticket_price=ticket_price2
            print(f'\n You have selected "{selected_movie}"')
            print(f'Ticket price: Rs.{ticket_price}')
            confirm=input('Do you want to book the ticket? (yes/no):')
            if confirm=='yes':
                print('Ticket booked successfully!')
            else:
                print('Booking cancelled.')
        else:
            print('Invalid movie choice.plz try again.')
    else:
        print('Sorry Invalid theater name.plz try again.')

#----------------------------------------------------------------------------------------------------------------------------#



 


    

