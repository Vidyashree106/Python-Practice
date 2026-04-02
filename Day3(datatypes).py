# Datatypes
#Integer datatype: without decimal value default=0
a=98
print(a)    # 98

a=98
print(type(a))  # <class 'int'>    

a=int()
print(a)    # 0

#Float datatype:number with decimal values default=0.0
b=98.48
print(b)    # 98.48

b=98.48
print(type(b))  # <class 'float'>  

b=float()
print(b)    # 0.0

#complex dataype:used to store combination of real and imaginary numbers
a=10+5j
print(a)    # 10+5j

a=11+6j
print(type(a))  # <class 'complex'>

c=complex()
print(c)    # 0j


z1=10+6j
z2=20+3j
result=z1+z2
print(result)   # (30+9j)

#Boolean dataype:it is used to check the condition where true=1 and flase=0
a=True
print(a)    # true

a=True
print(type(a))    

b=False
print(type(b))

a=True
b=98
print(a+b)

a=False
b=95
print(a*b)

e=bool()
print(e)
print(type(e))

#String(str):
s1='python'
print(s1)

s2='python' 
print(type(s2))

s3="HEllo python"
print(type(s3))

s4=''' Hello
welcome
to
python
class
'''
print(type(s4))






