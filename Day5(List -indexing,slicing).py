# List datatype- collection of homogeneous and heterogeneous elements
# Example for Homogeneous element
list1=[10,20,30,40,98]
print(list1)
print(type(list1))

# Example for Heterogenous element
list2=[98,'smith',True,100,98]
print(list2)
print(type(list2))

# Indexing on list collection
list=[10,'smith',98,100,'analayst']
print(list[0])
print(list[1])
print(list[3])
print(list[2])
print(list[-3])
print(list[-1])
print(list[9])

list3=[5,'Allen',30,108,'hello',50]
print(list3[0])
print(list3[1])
print(list3[2])
print(list3[5])
print(list3[-6])
print(list3[-5])
print(list3[6])
print(list3[-5])
print(list3[-4])
print(list3[-3])
print(list3[-9])


#Slicing on list collection
lst=[10,30,50,70,45,30,68,38]
print(lst[::])
print(lst[2:15:1])
print(lst[4:-1:1])
print(lst[::-1])
print(lst[5:7:1])
print(lst[3:7:-1])
print(lst[::2])
print(lst[-2::-2])

#Example for indexing using nested list
nested=[10,20,30,'smith',[100,200,300],'analayst']
print(nested[4])
print(nested[4][1])
print(nested[4][-1])
print(nested[4][1:-1:1])

#Example for slicing using nested list
nested=[10,'smith',[100,200,300,400,500],'analayst']
print(nested[2][1:5:1])
print(nested[2][3:4:2])
print(nested[1:5:1][2])


#Example positive slicing
list=[10,"python",3.14,"true",[1,2,4],(5,6)]
print(list[0:3:1])
print(list[1:4:1])
print(list[2:6:1])
print(list[3:7:1])
print(list[0:4:1])
print(list[2:7:1])
print(list[0:7:2])
print(list[1:6:2])
print(list[0:7:3])
print(list[4:7:1])

#Example Negative slicing
list=[10,"python",3.14,"true",[1,2,4],(5,6)]
print(list[-7:-4:1])
print(list[-6:-3:1])
print(list[-5:-2:1])
print(list[-4:-1:1])
print(list[-3:7:1])
print(list[-7:7:2])
print(list[-6:6:1])
print(list[-5:6:1])
print(list[-4:6:1])
print(list[-7:-1:1])
print(list[-6:6:2])

#Examplr for reverse slicing
list=[10,"python",3.14,"true",[1,2,4],(5,6)]
print(list[6::-1])
print(list[6:0:-1])
print(list[5:1:-1])
print(list[4:1:-1])
print(list[6:2:-2])
print(list[4::-1])






