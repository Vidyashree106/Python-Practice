# Exception handling 
# Syntax: 
        # try:
            # code that may raise exception
        # except:
            # code which is used to handel exception
        # else:
            # if there is no exception
        # finally:
            # it always runs

# Example to handle zero division
a=98
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print('We can not divide by zero')      # We can not divide by zero

#-----------------------------------------------------------------------------------------------------------------------------#

#  Example for type error
num1 = int(input('Enter the number:'))
num2 = input('Enter the number:')
try:
    result=num1+num2
    print(result)
except TypeError:
    print('invalid number')     

#-----------------------------------------------------------------------------------------------------------------------------#

# Example for value error
try:
    num=int(input('Enter the number:'))
    print(num)
except ValueError:
    print('invalid number')

#-----------------------------------------------------------------------------------------------------------------------------#

# Example for zerodivision and value error
try:
    num1=int(input('Enter the number:'))
    num2=int(input('Enter the number:'))
    print(num1/num2)
except ZeroDivisionError:
    print('cannot divide by zero')
except ValueError:
    print('invalid number')

#-----------------------------------------------------------------------------------------------------------------------------#

# Example for index error
try:
    li=[95,30,65]
    print(li[5])
except IndexError:
    print('Index out of range')

#-----------------------------------------------------------------------------------------------------------------------------#

# Example for try,except,else,finally block
try:
    a=98
    b=43
    result=a/b
except ZeroDivisionError:
    print('we cannot divide by zero')
else:
    print(f'result is :{result}')
finally:
    print('program completed')

#-----------------------------------------------------------------------------------------------------------------------------#



    