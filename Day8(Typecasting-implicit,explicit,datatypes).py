#Type casting
#types-1)Implicit typecasting 2)explicit typecasting
#Example for imlicit typecasting
a=98
b=35.67
print(a+b)      # 133.67000000000002

a=98
b=35.67
result=(a+b)
print(type(result))     # <class 'float'>

#Example for explicit typecasting
# 1)Integer datatype typecasting
num=57
print(float(num))     # 57.0
print(complex(num))   # 57+0j
print(bool(num))      # True
print(str(num))       # 57

print(list(num))    # typeError
print(tuple(num))   # typeError
print(set(num))     # typeError
print(dict(num))    # typeError

# 2)Float datatype typecasting
num=89.56
print(int(num))         # 89
print(complex(num))     # (89.56.0j)
print(bool(num))        # true
print(str(num))         # 89.56

print(list(num))       #typeError
print(tuple(num))      #typeError
print(set(num))        #typeError      
print(set(num))        #typeError      
print(dict(num))       #typeError

# 3)Complex datatype typecasting
a=10+0j
print(bool(a))
print(str(a))

print(int(a))        #typeError
print(float(a))
print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))

# 4)Boolean datatype typecasting
a=True
print(int(a))
print(float(a))
print(complex(a))
print(str(a))

print(list(a))       #typeError
print(tuple(a))
print(set(a))
print(dict(a))

# 5)String datatype typecasting
s1='python'
print(int(s1))        #valueError
print(float(s1))
print(complex(s1))
print(dict(s1))

print(list(s1))
print(tuple(s1))
print(bool(s1))
print(set(s1))

# 6)List datatype typecasting
l1=[10,20,'smith',98]
print(int(l1))       #typeError
print(float(l1)) 
print(complex(l1))
print(dict(l1))

print(bool(l1))
print(str(l1))
print(tuple(l1))
print(set(l1))

# 7)Tuple datatype typecasting
t1=(10,20,30,98)
print(int(t1))       #typeError
print(float(t1))
print(complex(t1))
print(dict(t1))

print(set(t1))
print(list(t1))
print(str(t1))
print(bool(t1))

# 8)Set datatype typecasting
s1={100,980,350,45}
print(int(s1))       #typeError
print(float(s1))
print(complex(s1))
print(dict(s1))

print(bool(s1))
print(str(s1))
print(list(s1))
print(tuple(s1))

# 9)Dictionary datatype typecasting
data={'ename':'smith','sal':98000}
print(int(data))         #typeError
print(float(data))
print(complex(data))

print(bool(data))
print(str(data))
print(list(data))
print(tuple(data))
print(set(data))

# ORD function in python
# used to convert character into AsCII
# syntax- ord(character)
print(ord('A'))
print(ord('a'))
print(ord('9'))

# CHR function in python
# used to convert ASCII into character
# syntax- chr(ASCII)
print(chr(65))
print(chr(95))
print(chr(98))
print(chr(57))

#WAP to convert upper case into lower case
character='A'
lower=chr(ord(character)+32)
print(lower)

#WAP to convert lower case to upper case
character='a'
upper=chr(ord(character)-32)
print(upper)







