# Conditional Statements
# if statement
# WAP to check greatest number among 2 numbers
a=78
b=45
if a>b:
    print(f'{a} is greatest number than {b}')    # 78 is greatest number than 45

# WAP to check the number is positive
num=int(input('Enter the number: '))
if num>0:
    print(f'{num} is a positive number')     # 78 is a positive number

# OR
num=45
if num>0:
    print(f'{num} is a positive number')     # 45 is a positive number

# WAP to check the number is even digit
num=44 
if num%2==0:
    print(f'{num} is an even number')       # 44 is an even number

# WAP to check the number is odd digit
num=45
if num%2!=0:
    print(f'{num} is an odd number')        # 45 is an odd number

# WAP to check the given number is divisible by 3 and 5
num=15
if num%3==0 and num%5==0:
    print(f'{num} is divisible by 3 and 5')     # 15 is divisible by 3 and 5

# WAP to check the given string start with vowel
s1='Air India'
if s1[0] in 'AEIOUaeiou':
    print(f'{s1} starts with vowel')       # Air India starts with vowel

# WAP to check the given string starts with consonants
s1='Air India'    
if s1[0] not in 'AEIOUaeiou':
    print(f'{s1} starts with consonant')      # ______

# WAP to check the given string starts with uppercase
s2='Microsoft'
if s2[0]>='A' and s2[0]<='Z':
    print(f'{s2} starts with uppercase')     # Microsoft starts with uppercase

# OR
s2='Microsoft'
if 'A'<=s2[0]<='Z':
    print(f'{s2} starts with uppercase')     # Microsoft starts with uppercase

# WAP to check the given data is single value datatype
data=45
if type(data) in [int,float,complex,bool]:
    print(f'{data} is a single value datatype')     # 45 is a single value datatype    

# WAP to check the given data is Collection datatype
data=[45, 67, 89]
if type(data) in [list, tuple, set, dict,str]:
    print(f'{data} is a Collection datatype')     # [45, 67, 89] is a Collection datatype

# WAP to check the given string having more than 5 characters
s1='education'
if len(s1)>5:
    print(f'{s1} having more than 5 characters')     # education having more than 5 characters

# WAP to check the number is divisible by 3 and 5.If it is convert into complex number
num=15
if num%3==0 and num%5==0:
    print(complex(num))     # 15+0j

# WAP to check the given nuumber is even ,if it is even then storw digits in list
num=498
if num%2==0:
    print(list(str(num)))   # ['4', '9', '8']

# WAP to check the character is vowel,if yes print the next character
ch='A'
if ch in 'AEIOUaeiou':
    next_ch=chr(ord(ch)+1)
    print(next_ch)     # B

# OR
ch='A'
vowels='AEIOUaeiou'
if ch in vowels:
    next_ch=chr(ord(ch)+1)
    print(next_ch)     # B

# WAP check the given character is consonant,if yes print the previous character  
ch='B'
if ch not in 'AEIOUaeiou':
    prev_ch=chr(ord(ch)-1)
    print(prev_ch)     # A

    
          
