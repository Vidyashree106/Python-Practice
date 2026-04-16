# for loop : 
# syntax :
# for variable in sequence:
#    #block of code
# statements

# WAP to print starting 5 natural numbers
for i in range(1,6):
    print(i) 
else:
    print('program completed')           # 1 2 3 4 5

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print all the items from list collection
li=['smith','king','scott']
for names in li:
    print(names)
# smith
# king
# scott

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print each character with iterations value using enumerate function
s1='python'
for iteration,ch in enumerate(s1,start=1):
    print(iteration,ch)

# 1 p
# 2 y
# 3 t
# 4 h
# 5 o
# 6 n    

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print even numbers from 1 to 10
for num in range(2,11,2):
    print(num)
# 2
# 4
# 6
# 8
# 10

#-----OR-------
for num in range(1,11):
    if num%2==0:
        print(num)

#-----OR-------
numbers=range(1,11)
for num in numbers:
    if num%2==0:
        print(num)        
    
#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print 10,20,30,40,50
for num in range(10,51,10):
    print(num)                              # 10
                                            # 20
                                            # 30
                                            # 40
                                            # 50    

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print even and odd numbers from 1 to 10
for num in range(1,11):
    if num%2==0:
        print(num,'even')
    else:
        print(num,'odd')                                            
# 1 odd
# 2 even
# 3 odd
# 4 even
# 5 odd
# 6 even
# 7 odd
# 8 even
# 9 odd
# 10 even    
    
#-----------------------------------------------------------------------------------------------------------------------------#

# WAp to print even  numbers from list collection
numbers=[10,11,17,98,45,38]
for num in numbers:
    if num%2==0:
        print(num)                              # 10
                                                # 98
                                                # 38   

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to calculate number of characters present in given string
s1='python'
count=0
for ch in s1:
    count+=1
print('number of characters present in string is :',count)   # number of characters present in string is : 6

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to calculate number of digits present in given number
num=47658
count=0
for digit in str(num):
    count=count+1
print(count)            # 5

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print sum of digits from given numbers
num=657879
total=0
for digit in str(num):
    total = total+int(digit)
print(f'Sum of all digits :{total}')            # Sum of all digits :42

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the hightest number from list collection
numbers=[10,11,17,98,45,38]
hightes=numbers[0]
for num in numbers:
    if num>hightes:
        hightes=num
print('hightest number from list collection is :',hightes)   # hightest number from list collection is : 98

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print sum of even digit from given number
num=657879
total=0
for digit in str(num):
    if int(digit)%2==0:
        total=total+int(digit)
print(f'sum of all digits:{total}')         # sum of all digits:14

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print sum of starting 10 natural numbers 
num=range(1,11)
total=0
for digit in num:
    total=total+digit
print(total)        # 55

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print factorial of number 5
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)  # 120

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print revers of given string
s='python'
rev=''
for ch in s:
    rev=ch+rev
print(rev)      # nohtyp

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print ASCII values of each character
s='python'
for ch in s:
    print(f'{ch}:{ord(ch)}')
# p:112
# y:121
# t:116
# h:104
# o:111
# n:110

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to calculate number of elements present in list collection
li=[10,45,78,95,40]
count=0
for value in li:
    count=count+1
print(count)            # 5

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find sum of number from list collection
li=[45,98,10,30]
total=0
for num in li:
    total=total+num
print(total)        # 183

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the highest number from list collection
li=[10,45,98,30]
highest=li[1]
for i in li:
    if i>highest:
        highest=i
print(f'Highest value is:{highest}')         #Highest value is:98

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the lowest number from list collection
li=[10,11,17,98,45,38]
lowest=li[0]
for num in li:
    if num<lowest:
        lowest=num
print('lowest number from list collection is :',lowest)     # lowest number from list collection is : 10

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print second_lowest number from list collection
numbers=[10,11,17,98,45,38]
lowest=numbers[0]
second_lowest=numbers[0]
for num in numbers:
    if num<lowest:
        second_lowest=lowest
        lowest=num
    elif lowest<num<second_lowest:
        second_lowest=num
print('second lowest number from list collection is :',second_lowest)   # second lowest number from list collection is : 11

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print the second hightest number from list collection
numbers=[10,11,17,98,45,38]
hightes=numbers[0]
second_hightes=numbers[0]
for num in numbers:
    if num>hightes:
        second_hightes=hightes
        hightes=num
    elif second_hightes<num<hightes:
        second_hightes=num
print('second hightest number from list collection is :',second_hightes)   # second hightest number from list collection is : 45

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print alphabets and digits present in the given string
s1='p12y34thon56'
alphabets=''
digits=''
for ch in s1:
    if ('A'<=ch<='Z') or ('a'<=ch<='z'):
        alphabets=alphabets+ch
    elif '0'<=ch<='9':
        digits=digits+ch
print('alphabets present in string are :',alphabets)   # alphabets present in string are : python
print('digits present in string are :',digits)         # digits present in string are : 123456

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given string is palindrome or not
text='eye'
rev=''
for ch in text:
    rev=ch+rev
if text==rev:
    print('it is a palindrome')     # it is a palindrome
else:
    print('not a palindrome')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to store the charactes from one string to another string
s='education'
s1=''
for ch in s:
    s1=s1+ch
print(s1)   # education   

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print alphabets from given string
s1='P123ython'
res=''
for ch in s1:
    if ('A'<= ch <= 'Z') or ('a' <= ch <= 'z'):
        res=res+ch
print(res)        # Python

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print alphabets and digits from given string
s='P123ython'
res=''
digit=''
for ch in s:
    if ('A'<=ch<='Z') and ('a'<=ch<='z'):
        res=res+ch
    elif ('0'<= ch <= '9'):
        digit=digit+ch
print(res)      # python
print(digit)    # 123

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to convert upper case into lower case
s='PYTHON'
res=''
for ch in s:
    res=res+chr(ord(ch)+32)
print(res)      # python

#-----------------------------------------------------------------------------------------------------------------------------#
 
# WAP to print all vowels from the given string
s='education'
vowels=''
for ch in s:
    if ch in 'AEIOUaeiou':
        vowels=vowels+ch
print(vowels)   # euaio

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to convert upper case vowel into lowercase
s='EducAtION'
vowels=''
for ch in s:
    if ch in 'AEIOU':
        vowels=vowels+chr(ord(ch)+32)
print(vowels)       # eaio

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to print special character from given string
s='python@123#s'
res=''
for ch in s:
    if not ('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9'):
        res=res+ch
print(res)  # @#

#-----------------------------------------------------------------------------------------------------------------------------#

#WAP to extract vowels and consonants from given string
s='education'
vowels=''
consonants=''
for ch in s:
    if ch in 'AEIOUaeiou':
        vowels=vowels+ch
    elif ch not in 'AEIOUaeiou':
        consonants=consonants+ch
print(vowels)       # euaio
print(consonants)       # dctn

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to extract vowels,consonants,digit from given string
s='education1237'
vowels=''
consonants=''
digit=''
for ch in s:
    if ch in 'AEIOUaeiou':
        vowels=vowels+ch
    elif '0'<=ch<='9':
        digit=digit+ch
    elif ch not in 'AEIOUaeiou':
        consonants=consonants+ch
print(vowels)       # euaio
print(consonants)       # dctn
print(digit)       # 1237

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is palindrome or not
number=121
rev=0
for i in str(number):
    rev=rev*10+int(i)
if number==rev:
    print(f'{number} is palindrome')        # 121 is palindrome
else:
    print(f'{number} is not palindrome')

#-----------------------------------------------------------------------------------------------------------------------------#    

# WAP to check the given number is prime number or not 
n=6
for i in range(2,n):
    if n%i==0:
        print(f'{n} is Not a prime number')
        break
else:
    print(f'{n} is not a prime number')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is armstronng number or not
n=153
temp=n
sum_cubes=0
length=len(str(n))
for i in str(n):
    sum_cubes=sum_cubes+int(i)**length
if temp==sum_cubes:
    print(f'{temp} is armstrong number')
else:
    print(f'{temp} is not a armstrong number')      # 153 is armstrong number

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is perfect number or not
num=6
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(f'{num} is perfect number')       # 6 is perfect number
else:
    print(f'{num} is not perfect number')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is strong number are not
num=149
sum=0
for n in str(num):
    fact=1
    for i in range(1,int(n)+1):
        fact=fact*i
    sum=sum+fact
if sum==num:
    print('Strong number')      # Strong number
else:
    print('Not a strong number')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is spy number or not
num=1124
sum=0
product=1
for i in str(num):
    sum=sum+int(i)
    product=product*int(i)
if sum==product:
    print('Is a spy number')        # Is a spy number
else:
    print('Not a spy number')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is neon number or not
num=9
square=num*num
sum=0
for n in str(square):
    sum=sum+int(n)
if sum==num:
    print('Neon number')        # Neon number
else:
    print('Not a neon number')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to remove duplicate characters from given string
s='apple'
rem=''
for ch in s:
    if ch not in rem:
        rem=rem+ch
print(rem)

#-----------------------------------------------------------------------------------------------------------------------------#
    
