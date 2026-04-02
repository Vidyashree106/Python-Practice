# Indexing on string collection datatype  i)+ve indexing  ii)-ve indexing   
#Syntax:variablename[index_value]
msg='python'
print(len(msg))

msg='python'
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])
print(msg[4])
print(msg[5])
print(msg[-3])
print(msg[-5])
print(msg[-6])
print(msg[6]) # error bcz string out of range

string="Welcome to python"
print(string[1])
print(string[2])
print(string[3])
print(string[6])
print(string[7])
print(string[8])
print(string[9])
print(string[10])
print(string[14])
print(string[16])

#Slicing in python: process of exracting multiple characters i)+ve slicing  ii)-ve slicing iii)revers slicing 
#in all 3 start index is include
#in all 3 end index is excluded
#[startvalue:Endvalue:Stepvalue]
#Stepvalue:according to value it will jump to next letter
msg='Welcome to python'
print(msg[::])
print(msg[2:13:1])
print(msg[4:15:2])
print(msg[-16:-3:1])
print(msg[::-1])

#to print even digit character in forward direction
string="python class"
print(string[0::2])

#to print odd digit character in forward direction
string='python class'
print(string[1::2])

#to print even digit character in backward direction
string='python class'
print(string[-2::-2])

#to print odd digit character in backward direction
string='python class'
print(string[-1::-2])

#to revers a given string
string='python class'
print(string[::-1])

#Example for Positive slicing
string='Welcome to Python class'
print(string[0:7])
print(string[8:10])
print(string[11:17])
print(string[18:23])
print(string[0:11])
print(string[11:23])
print(string[3:9])
print(string[5:15])
print(string[:7])
print(string[8:])

#Example for negative slicing
string='Welcome to Python class'
print(string[-5:])
print(string[-12:-6])
print(string[-12:-6])
print(string[-23:-16])
print(string[-15:-13])
print(string[-11-7])
print(string[-23:-1])
print(string[:-6])
print(string[-6:])
print(string[-10:-5])