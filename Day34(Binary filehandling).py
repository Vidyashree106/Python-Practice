# binary file handling
# write binary data into a file
file=open('data.bin','wb')
data=b'Hello students'
file.write(data)
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# Read binary data into a file
file=open('data.bin','rb')
data=file.read()
print(data)
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

file=open('# paste the link # ','rb')
data=file.read()
print(data)
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#