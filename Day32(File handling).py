# File handling
# 1) text file
# 2) CSV file
# 3) Binary file

# 1) text file
# Syntax for file handling without with statement
# file_object = oepn('filename.exe','mode')
# # perform operations
# file_object.close()

# Types of mode
# 1)w(write) mode   2) r(read) mode     3) a(append) mode      4) w+(write and read) mode       5) r+(read and write) mode
# 6)a+(write and read) mode        7)x(it is used to create new file)

# 1) w mode
file=open('python118.txt','w')
file.write('Hello students welcome to python class')
file.close() 

#-----------------------------------------------------------------------------------------------------------------------------#

# 2) r mode
file=open('python118.txt','r')
print(file.read())      # Hello students welcome to python class
file.close() 

#-----------------------------------------------------------------------------------------------------------------------------#

# 3) a mode
file=open('python118.txt','a')
file.write('\n Appending new text using append')
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# 4) w+ mode
file=open('python118.txt','w+')
file.write('Hello students')
file.seek(0)
print(file.read())      # Hello students
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# 5) r+ mode
file=open('python118.txt','r+')
print(file.read())
file.write('\n We are using r+ mode')
file.seek(0)
print(file.read())      # Hello students
                        # We are using r+ mode
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# 6) a+ mode
file=open('python118.txt','a+')
file.write('\n appending new data using a+')
file.seek(0)
print(file.read())

#-----------------------------------------------------------------------------------------------------------------------------#

# 7) x mode
file=open('java.txt','x')
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# using with statement
# Syntax : with open('filename.exe','mode') as file:
    # operations

# WAP to read the content of the file using with statement
with open('Pythonbatch.txt','w') as file:
    file.write('Hello Students')    

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to read the content of the file using with statement
with open('Pythonbatch.txt','r') as file:
    content=file.read()
    print(content)          # Hello Students

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to append new data to the existing file using with statement
with open('Pythonbatch.txt','a') as file:
    file.write('\n adding new text')    

# WAP to write data and then read data using with statement
with open('Pythonbatch.txt','w+') as file:
    file.write('we are using w+ mode')
    file.seek(0)
    content=file.read()
    print(content)          # we are using w+ mode

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to read existing content and then write new content and read entire content
with open('Pythonbatch.txt','r+') as file:
    print('before adding new data reading content')
    print(file.read()) 
    file.write('\n add new data')
    file.seek(0)
    print('after adding new data reading content')
    print(file.read())      # before adding new data reading content
                            # we are using w+ mode

                            # after adding new data reading content
                            # we are using w+ mode
                            # add new data  

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to append  data and then read entire content using with statement
with open('Pythonbatch.txt','a+') as file:
    file.write('\n we are appending new data')
    file.seek(0)
    print(file.read())          # we are using w+ mode
                                # add new data
                                # we are appending new data

#-----------------------------------------------------------------------------------------------------------------------------#

# Types of read mode
# read()
with open('Pythonbatch.txt','r') as file:
    print(file.read())          # we are using w+ mode
                                # add new data
                                # we are appending new data

#-----------------------------------------------------------------------------------------------------------------------------#

#  Example to read starting 5 characters
with open ('Pythonbatch.txt','r') as file:
    print(file.read(5))         # we ar

#-----------------------------------------------------------------------------------------------------------------------------#

# Example to read first line
with open('Pythonbatch.txt','r') as file:
    print(file.readline())      # we are using w+ mode

#-----------------------------------------------------------------------------------------------------------------------------#

# Example to read all the lines and return into list of string
with open('Pythonbatch.txt','r') as file:
    print(file.readlines())     # ['we are using w+ mode\n', ' add new data\n', ' we are appending new data']

# ----OR----

with open('Pythonbatch.txt','r') as file:
    print(file.readlines()[2])     #  we are appending new data

#-----------------------------------------------------------------------------------------------------------------------------#

# Write a program (WAP) to develop a student record management system using Python file handling (students.txt) with the following functionalities:
# Task 1: Add Students
# Write a function to add student details (name, age, course) and store the data in a text file in the given format:(name, age, course)

# Task 2: Display Student Details

# Task 3: Find Student Details

# Task 4: Delete Student Details

# Task 5: Create a menu with the following options:
# 1) Add Student
# 2) Display Student
# 3) Find Student
# 4) Delete Student
# 5) Exit    

def add_student():
    file = open('students.txt', 'a')
    name = input('Enter student name: ')
    age = input('Enter age: ')
    course = input('Enter course: ')

    file.write(name + '\n')
    file.write(age + '\n')
    file.write(course + '\n')
    file.write('-----\n')
    file.close()

    print('Student added successfully!\n')

def view_students():
    file = open('students.txt', 'r')
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print('No records found.\n')
        return

    print('\nStudent Records:')

    i = 0
    while i < len(lines):
        name = lines[i]
        age = lines[i+1]
        course = lines[i+2]

        print('Name:', name, 'Age:', age, 'Course:', course)
        i += 4

    print()

def search_students():
    name_to_search = input('Enter name to search: ')

    file = open('students.txt', 'r')
    lines = file.readlines()
    file.close()

    i = 0
    while i < len(lines):
        name = lines[i]

        if name.lower().startswith(name_to_search.lower()):
            age = lines[i+1]
            course = lines[i+2]

            print('Record found:')
            print('Name:', name, 'Age:', age, 'Course:', course)
            return

        i += 4

    print('Student not found.\n')

def delete_student():
    name_to_delete = input('Enter name to delete: ')

    file = open('students.txt', 'r')
    lines = file.readlines()
    file.close()

    new_lines = []

    i = 0
    while i < len(lines):
        name = lines[i]

        if name.lower().startswith(name_to_delete.lower()):
            i += 4   # skip record
        else:
            new_lines.append(lines[i])
            new_lines.append(lines[i+1])
            new_lines.append(lines[i+2])
            new_lines.append(lines[i+3])
            i += 4

    file = open('students.txt', 'w')
    file.writelines(new_lines)
    file.close()

    if len(lines) == len(new_lines):
        print('Student not found.\n')
    else:
        print('Student deleted successfully!\n')

def menu():
    while True:
        print('1. Add Student')
        print('2. View Student')
        print('3. Search Student')
        print('4. Delete Student')
        print('5. Exit')

        choice = input('Enter choice: ')

        if choice == '1':
            add_student()

        elif choice == '2':
            view_students()

        elif choice == '3':
            search_students()

        elif choice == '4':
            delete_student()

        elif choice == '5':
            print('Exiting program...')
            break

        else:
            print('Invalid choice\n')
menu()

#-----------------------------------------------------------------------------------------------------------------------------#
