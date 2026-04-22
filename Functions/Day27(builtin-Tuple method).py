# Tuple method in python
# count method:
t1=(0,30,20,30,40,30)
print(t1.count(30))     # 3

t2=('smith',98.100,'smith')
print(t2.count('smith'))        # 2

#-----------------------------------------------------------------------------------------------------------------------------#

# index method
t1=(10,20,30,20,50,20)
print(t1.index(20))     # 1

t1=(10,20,30,20,50,20)
first=t1.index(20)
second=t1.index(20,first+1)
print(second)       # 3

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to find the position of third occurance element from tuple collection using enumerate function
t1=(10,20,30,20,50,20,98)
element=20
count=0
for index,value in enumerate(t1):
    if value==element:
        count=count+1
        if count==3:
            print(f'Third occrance :{index}')       # Third occrance :5
            break

#-----------------------------------------------------------------------------------------------------------------------------#


