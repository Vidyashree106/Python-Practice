# Arithemetic operator
# (+, -, *, /, //, %, **)

# 1)Addition(+)
a=98
b=76
result=98+76
print(f'sum of {a} and {b} is: {result}')    # sum of 98 and 76 is: 174

x=67
y=56.89
print(x+y)      # 123.89

msg='Smith is earning '
sal=9800
print(msg+str(sal))     # Smith is earning 9800  

l1=[10,20,30]
l2=[40,50,60]
print(l1+l2)        # [10, 20, 30, 40, 50, 60]

num1=100
num2=10+5j
print(num1+num2)        # (110+5j)

t1=(1,2,3)
t2=(10,20,30)
print(t1+t2)        # (1, 2, 3, 10, 20, 30)

# 2)Subtraction(-)
n=98
m=67
print(n-m)      # 31

# 3) Multiplication(*)
print(3*2)      # 6
print(4*' python')      #  python python python python

# 4)true division(/)
a=98
b=78
print(a/b)      # 1.2564102564102564

# 5) Floor division(//)
a1=78
b1=34
print(a1//b1)   # 2

# WAP to remove last digit from the given number
n1=8734567
print(n1//10)    # 873456 

# WAP to remove last 2 digit from the given number
n1=8734567
print(n1//100)  # 87345

# 6)Modulas(%)
a=11
b=2
print(a%b)      # 1

n1=56
n2=0
print(n1%n2)    # ZeroDivisionError: division by zero

# WAP to display last digit from given number
number=7689
print(number%10)     # 9

# WAP to display last 3 digits from the given  number
number=7689
print(number%1000)      # 689

# 7)Exponent(**(power))
a=2
b=3
print(a**b)     # 8=2*2*2