#Set datatype 
s1={10,20,30,20,20,40,98}
print(s1)
print(type(s1))

# Example of indexing on set collection
s={100,980,400,390,578}
print(s[3])
li=list(s)
print(li)
print(li[3])

#Dictionary datatype
data={'ename':'smith','sal':98000,'job':'analyst'}
print(type(data))

print(data['ename'])
print(data['sal'])
print(data['job'])

#or can be print using below

print(f'employee name : {data["ename"]} and salary : {data["sal"]} working as : {data["job"]}')

#WAP to store multiple employee information
employee={
    'emp1':{'ename':'smith' , 'sal':900},
    'emp2':{'ename':'king' , 'sal':2000},
    'emp3':{'ename':'allen' , 'sal':1250}
}
print(employee['emp3'])
print(employee['emp3']['ename'])


# Range dataype
coll=range(6)
print(coll)
print(type(coll))
print(list(coll))

#Example 1
r1=range(10,16)
print(list(r1))

#Example 2
r2=range(1,11,2)
print(list(r2))

#Example 3
r3=range(10,5,-1)
print(list(r3))

#Example 4
nums=range(10,56,6)
print(type(nums))

#Example for indexing using range dataype 
nums=range(100,501,100)
print(list(nums))   #[100, 200, 300, 400, 500]  
print(nums[0])
print(nums[1])
print(nums[3])
print(nums[2])
print(nums[4])
print(nums[7])