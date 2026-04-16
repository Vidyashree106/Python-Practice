# WAP to find the ASCII value of single character
ch='a'
value=ord(ch)
print(f'ASCII value of {ch} is:{value}')        # ASCII value of a is:97

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to print ASCII value of all the character in the string
string='Python'
i=0
while i<len(string):
    value=ord(string[i])
    print(f'ASCII value of {string[i]} is: {value}')
    i=i+1
# ASCII value of P is: 80
# ASCII value of y is: 121
# ASCII value of t is: 116
# ASCII value of h is: 104
# ASCII value of o is: 111
# ASCII value of n is: 110    

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to concatinate string
s1='Python'
s2=' Full stack'
value=s1+s2
print(f'Concatenation of {s1} and {s2} is:{value}')         # Concatenation of Python and  Full stack is:Python Full stack

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to convert string to upper case
s1='python'
i=0
res=' '
while i<len(s1):
    if s1[i]>='a' and s1[i]<='z':
        res=res+chr(ord(s1[i])-32)
    else:
        res=res+s1[i]
    i=i+1
print(res)                  #  PYTHON

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to convert string to lower case

s1='PYTHON'
i=0
res=' '
while i<len(s1):
    if s1[i]>='A' and s1[i]<='Z':
        res=res+chr(ord(s1[i])+32)
    else:
        res=res+s1[i]
    i=i+1
print(res)                      # python

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to count the occurence of a character in a string

s='pythonpy'
ch='y'
i=0
count=0
while i<len(s):
    if s[i]==ch:
        count=count+1
    i=i+1
print(count)            # 2

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to count total character in a string
s='python'
i=0
count=0
while i<len(s):
    count=count+1
    i=i+1
print(count)            # 6

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to count total number of words in a string
s='python is a programming language'
i=0
count=1
while i<len(s):
    if s[i]==' ':
        count=count+1
    i=i+1
print(count)            # 5

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to count vowels string
s='python'
i=0
count=0
while i<len(s):
    if s[i] in 'aeiouAEIOU':
        count=count+1
    i=i+1
print(count)            # 1

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to count vowels and consonants in a string
s='python'
i=0
vowels=0
consonants=0
while i<len(s):
    if s[i] in 'aeiouAEIOU':
        vowels=vowels+1
    else:
        consonants=consonants+1
    i=i+1
print(f'Vowels: {vowels}')          # Vowels: 1
print(f'Consonants: {consonants}')  # Consonants: 5

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to count alphabet, digit and special character in a string
s='python@123'
i=0
alphabet=0
digit=0
special_char=0
while i<len(s):
    if s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z':
        alphabet=alphabet+1
    elif s[i]>='0' and s[i]<='9':
        digit=digit+1
    else:
        special_char=special_char+1
    i=i+1
print(f'Alphabet: {alphabet}')                    # Alphabet: 6
print(f'Digit: {digit}')                           # Digit: 3  
print(f'Special Character: {special_char}')          # Special Character: 1

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given string is palindrome or not
s='madam'   
i=0
res=''
while i<len(s):
    res=s[i]+res
    i=i+1
if s==res:
    print(f'{s} is a palindrome string')          # madam is a palindrome string
else:
    print(f'{s} is not a palindrome string')

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to print character from a sting
s='python'
i=0
while i<len(s):
    print(s[i])
    i=i+1
# p
# y 
# t
# h
# o
# n

#---------------------------------------------------------------------------------------------------------------------------#

# WAP remove vowels from given string
s='python'
i=0
res=''
while i<len(s):
    if s[i] not in 'aeiouAEIOU':
        res=res+s[i]
    i=i+1
print(res)              # pythn

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to print even number elements from list collection
l=[1,2,3,4,5,6]
i=0
while i<len(l):
    if l[i]%2==0:
        print(l[i])
    i=i+1
# 2
# 4
# 6

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to print 2nd largest number from given list
l=[1,2,3,4,5,6]
largest=l[0]
second_largest=l[0]
i=0
while i<len(l):
    if l[i]>largest:
        second_largest=largest
        largest=l[i]
    elif l[i]>second_largest and l[i]!=largest:
        second_largest=l[i]
    i=i+1
print(second_largest)          # 5

#---------------------------------------------------------------------------------------------------------------------------#

# WAP to toggle given string
s1='PyTHon'
s2=''
i=0
while i<len(s1):
    if s1[i]>='A' and s1[i]<='Z':
        s2=s2+chr(ord(s1[i])+32)
    elif s1[i]>='a' and s1[i]<='z':
        s2=s2+chr(ord(s1[i])-32)
    else:
        s2=s2+s1[i]
    i=i+1
print(s2)              # pYthON

#---------------------------------------------------------------------------------------------------------------------------#

