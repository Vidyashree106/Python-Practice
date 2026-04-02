#Tuple datatype in python, should enclose with(paranthesis), it is immutable, separated by ","
#Examples
t1=(10)
print(type(t1))

t2=(10,)
print(type(t2))

#example for homogeneous Collection
t3=(10,20,30,98)
print(t3)
print(type(t3))

#Example for heterogeneous Collection
t4=(10,'smith',98.45,True,(1,2,3),[98,100])
print(type(t4))

#Indexing on tuple datatype
#syntax:variablename[index value]
tuple=(100,900,500,400,350,980,298)
print(tuple[0])
print(tuple[3])
print(tuple[1])
print(tuple[-1])
print(tuple[9])
print(tuple[-7])
print(tuple[-3])

#Slicing on tuple datatype
#syntax:variablename[start-index,end-index,step-value]
tuple=(100,900,500,400,350,980,298)
print(tuple[::])
print(tuple[2:6:1])
print(tuple[5:2:1])
print(tuple[::-1])
print(tuple[-3:-7:-1])
print(tuple[2::2])
print(tuple[-2::-2])
print(tuple[1::2])
print(tuple[-1::-2])

#Example for positive slicing
t1=(900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[0:5:1])
print(t1[1:7:1])
print(t1[2:8:2])
print(t1[0:9:3])
print(t1[3:9:2])
print(t1[4:9:1])
print(t1[1:9:2])
print(t1[0:8:4])
print(t1[2:9:3])

#Example for negative slicing
t1=(900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[-9:-1:1])
print(t1[-8:-2:1])
print(t1[-7:-1:3])
print(t1[-6:-2:1])
print(t1[-5:-1:2])
print(t1[-9:-3:2])
print(t1[-8:-1:1])
print(t1[-7:-3:2])
print(t1[-6:-1:2])
print(t1[-4:-1:1])

#Example for revers slicing
print(t1[8:0:-1])
print(t1[8:2:-2])
print(t1[7:1:-1])
print(t1[8:-1:-1])
print(t1[6:0:-2])
