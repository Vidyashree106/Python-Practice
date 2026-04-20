# list collection method
# append method
# syntax : variablename.listmethod(element)
new_list=[45,98,100]
new_list.append(50)
print(new_list)     # [45, 98, 100, 50]      

li=['smith',98]
li.append([100,200,150])
print(li)       # ['smith', 98, [100, 200, 150]]

#--------------------------------------------------------------------------------------------------------------------------------------#

# extend method
# syntax : variablename.listmethod(element)
li=['smith',98]
li.extend([100,200,150])
print(li)           # ['smith', 98, 100, 200, 150]

#--------------------------------------------------------------------------------------------------------------------------------------#

# insert method
# syntax : variablename.listmethod(index,element)
li=[20,40,89,50]
li.insert(2,90)
print(li)       # [20, 40, 90, 89, 50]

#--------------------------------------------------------------------------------------------------------------------------------------#

# count method
# syntax : variablename.count(element)
li=[10,20,30,40,20,50,60,20,70,90]
res=li.count(20)
print(res)          # 3

#--------------------------------------------------------------------------------------------------------------------------------------#

# index method
# syntax : variablename.index(element)
li=[10,20,30,20,20]
print(li.index(20))         # 1

#--------------------------------------------------------------------------------------------------------------------------------------#

#reverse method
# syntax : variablename.reverse()
li=[1,2,7,5,6]
li.reverse()
print(li)       # [6, 5, 7, 2, 1]

#--------------------------------------------------------------------------------------------------------------------------------------#

# sort method
# syntax : variablename.sort()
# for ascending order
li=[10,9,45,98,38,47]
li.sort()
print(li)       # [9, 10, 38, 45, 47, 98]

#--------------------------------------------------------------------------------------------------------------------------------------#

# for descending order
li=[10,9,45,98,38,47]
li.sort(reverse=True)
print(li)           # [98, 47, 45, 38, 10, 9]

#--------------------------------------------------------------------------------------------------------------------------------------#

# pop method
# syntax : variablename.pop()
li=[10,9,45,98,38,47]
li.pop()
print(li)       # [10, 9, 45, 98, 38]

li=[10,9,45,98,38,47]
li.pop(3)
print(li)       # [10, 9, 45, 38, 47]

#--------------------------------------------------------------------------------------------------------------------------------------#

# remove method
# syntax : variablename.remove(element)
li=[10,30,20,30,45,30]
li.remove(30)
print(li)       # [10, 20, 30, 45, 30]

#--------------------------------------------------------------------------------------------------------------------------------------#

# clear method
# syntax : variablename.clear()
li=[10,20,30,47,78]
li.clear()
print(li)       # []

#--------------------------------------------------------------------------------------------------------------------------------------#

# WAP to find position of 4th occurence of element using enumerate function
data=[10,20,30,20,40,20,50,20,98]
element=20
count=0
for index,value in enumerate(data):
    if value==element:
        count=count+1
    if count==4:
        print(index)        # 7
        break

#--------------------------------------------------------------------------------------------------------------------------------------#    

# WAP to find 3rd highest element using enumerate function
data=[10,20,30,20,40,20,50,20,98]
numbers=list(set(data))
numbers.sort(reverse=True)

for index,value in enumerate(numbers,start=1):
    if index==3:
        print(f'third highest element:{value}')     # third highest element:40
        break

#--------------------------------------------------------------------------------------------------------------------------------------#
    
# WAP to separate even number and odd number element from list collection
nums=[10,15,20,25,30,40,45]
even=[]
odd=[]
for num in nums:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(f'even numbers:{even}')       # even numbers:[10, 20, 30, 40]
print(f'odd numbers:{odd}')         # odd numbers:[15, 25, 45]

#--------------------------------------------------------------------------------------------------------------------------------------#

# WAP to check the given number is palindrome,armstrong number,strong number using only one while loop and one block
num=int(input('Enter the number:'))
original=num
temp=num
rev=0
armstrong=0
strong=0
length=len(str(temp))
while temp>0:
    digit=temp%10

    rev=rev*10+digit

    armstrong=armstrong+digit**length

    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    strong=strong+fact

    temp=temp//10    

print(f'{num} is {'a palindrome number' if rev==original else 'not a palindrome number'}')        
print(f'{num} is {'a armstrong number' if armstrong==original else 'not a armstrong number'}')   
print(f'{num} is {'a strong number' if strong==original else 'not a strong number'}')     

# 121 is not a palindrome number
# 121 is not a armstrong number
# 121 is not a strong number

# 153 is not a palindrome number
# 153 is a armstrong number
# 153 is not a strong number

# 145 is not a palindrome number
# 145 is not a armstrong number
# 145 is a strong number

#--------------------------------------------------------------------------------------------------------------------------------------#