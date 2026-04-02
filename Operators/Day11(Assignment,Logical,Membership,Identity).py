# WAP to swap two numbers without using third variable
a=100
b=200
print(f'before swaping:{a}')
print(f'before swaping:{b}')
a,b=b,a
print(f'after swaping:{a}')
print(f'after swaping:{b}')

# WAP to swap two numbers using third variable
a=100
b=200
print(f'before swaping:{a}')
print(f'before swaping:{b}')
temp=a
a=b
b=temp
print(f'after swaping:{a}')
print(f'after swaping:{b}')

# Assignment operators
# Compound assignment operators(+=, -=, *=, /=, //=, %=, **=)
# for '+=' operator
a=98
a+=2
print(a)    # 100

# for '-=' operator
a=98    
a-=2
print(a)    # 96

# for '*=' operator
a=98
a*=2
print(a)    # 196

# for '/=' operator
a=11
a/=3
print(a)    # 3.6

# for '//=' operator
a=11
a//=3
print(a)    # 3

# for '%=' operator
a=11
a%=3
print(a)    # 2

# for '**=' operator
a=20
a**=3
print(a)    # 8000

#Logical operators
# and, or, not
# Example 1
a=10
b=50
c=60
print(a<b and b<c)     # True
print(a<b and b>c)      # False
print(a>b or b<c)      # True
print(a==b or a<c)     # True

# Example 2
a=10
b=50
c=60
d=100
print(a<b and b<c and c<d and d>a)     # True

# Example 3
a=0
print(not (a))   # True
a=1
print(not (a))   # False

# Example 4
a=5
print(not (a>1))    # False

# Example 5
a=50
b=45
print(not (a>b or b<a))     # False

# Membership operators
# in, not in
s1='python'
print('p' in s1)    # True
print('P' in s1)    # False
print('th' in s1)   # True
print('python' in s1)    # True
print('Python' in s1)    # False

print('p' not in s1)    # False
print('P' not in s1)    # True
print('j' not in s1)   # True
print('python' not in s1)    # False
print('Python' not in s1)    # True

# Example on list
list=[10,20,98,48]
print(10 in list)   # True
print(100 in list)  # False
print(98 in list)   # True

# Example on tuple
tuple=(1,28,'smith')
print(28 in tuple)     # True
print('smith' in tuple)    # True
print(100 in tuple)    # False

# Example on set
set={25,30,48}
print(25 in set)     # True
print(100 in set)    # False
print(48 in set)     # True

# Example on set dictionary
data={'ename':'smith','sal':900}
print('smith' in data)   # True
print('sal' in data)     # True
print('job' in data)     # False

print('smith' not in data)   # False
print('karna' not in data)    # True
print(900 not in data)     # False

# Identity operators
# is, is not
a=98
b=98
print(a is b)     # True
print(a is not b) # False

list1=[10,20,30]
list2=[10,20,30]
print(list1 is list2)     # False
print(list1 is not list2) # True

