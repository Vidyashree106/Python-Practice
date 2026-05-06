# Global variables
# Accessing global variables inside function
num=98
def function():
    print(f'Value is:{num}')            # Value is:98
function()

#-----------------------------------------------------------------------------------------------------------------------------#

# Accessing global variables inside function and outside the function
num=98
def function():
    print(f'Accessing inside the function:{num}')       # Accessing inside the function:98
function()
print(f'Accessing outside the function:{num}')          # Accessing outside the function:98

#-----------------------------------------------------------------------------------------------------------------------------#

# For modifing global variable
num=98
def fun():
    global num
    num=num+1
    print(f'After updating value:{num}')        # After updating value:99
fun()
print(f'Outside accessing:{num}')               # Outside accessing:99

#-----------------------------------------------------------------------------------------------------------------------------#

# Local Variable
def fun():
    num=98
    print(f'Value is :{num}')       # Value is :98
fun()

#-----------------------------------------------------------------------------------------------------------------------------#

# Accessing local variable outside the function
def fun():
    num=98
    print(f'value is:{num}')        # value is:98
fun()
print(f'Outside function:{num}')    # Outside function:99

#-----------------------------------------------------------------------------------------------------------------------------#

# Accessing local variable outside function and modify value of local variable
def outer():
    num=98
    def inner():
        nonlocal num
        num=num+1
        print(f'inside function after updating :{num}')                 # inside function after updating :99
    inner()
    print(f'Outside function accessing local variable:{num}')           # Outside function accessing local variable:99
outer()

#-----------------------------------------------------------------------------------------------------------------------------#

# 1) General copy (normal copy)
# General copy (normal copy)
a=[10,30,98]
b=a
print(a)            # [10, 30, 98]
print()
print(b)            # [10, 30, 98]

#-----------------------------------------------------------------------------------------------------------------------------#

# modifying original list collection
a[1]=45
print(f'After modify original:{a}')         # After modify original:[10, 45, 98]
print()
print(f'After modify copied:{b}')           # After modify copied:[10, 45, 98]

#-----------------------------------------------------------------------------------------------------------------------------#

# 2) Shallow copy
import copy
original_list=[[1,2,3],[4,5,6,7]]
shallow_copy_list=copy.copy(original_list)
print(original_list)        # [[1, 2, 3], [4, 5, 6, 7]]
print()
print(shallow_copy_list)    # [[1, 2, 3], [4, 5, 6, 7]]

#-----------------------------------------------------------------------------------------------------------------------------#

# modify nested list elements
shallow_copy_list[1][3]=98
print(original_list)        # [[1, 2, 3], [4, 5, 6, 98]]
print()
print(shallow_copy_list)        # [[1, 2, 3], [4, 5, 6, 98]]

#-----------------------------------------------------------------------------------------------------------------------------#

# 3) Deep copy()
import copy
original_list=[[1,2,3],[4,5,6,7]]
deep_copy_list=copy.deepcopy(original_list)
print(original_list)        # [[1, 2, 3], [4, 5, 6, 7]]
print()
print(deep_copy_list)       # [[1, 2, 3], [4, 5, 6, 7]]
print()

#-----------------------------------------------------------------------------------------------------------------------------#

