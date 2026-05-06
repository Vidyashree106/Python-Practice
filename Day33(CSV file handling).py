# CSV file handling(Comma separated value)
# Syntax : Without with statement
    # import csv
    # file=open('filename.csv','mode')
    # # operations
    # file.close()

# Using with statement
    # import csv
    # with open('filename.csv','mode') as file:
    # # operations

# WAP to store employee name and salary using csv file handling
import csv
file=open('python.csv','w',newline='')
writer=csv.writer(file)
writer.writerow(['ename','sal'])
writer.writerow(['smith',98000])
writer.writerow(['king',45000])
writer.writerows([['allen',98000],['jones',4700]])
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to read CSV file
import csv
file=open('python.csv','r')
reader = csv.reader(file)
for row in reader:
    print(row)              # ['ename', 'sal']
file.close()                # ['smith', '98000']
                            # ['king', '45000']
                            # ['allen', '98000']
                            # ['jones', '4700']

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to appen new data  to the csv file
import csv
file=open('python.csv','a')
append=csv.writer(file)
append.writerow(['martin',89000])
file.close()   

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to read and write operations on csv file using w+ mode
import csv
file=open('main.csv','w+')
writer=csv.writer(file)
writer.writerow(['ename','sal'])
writer.writerow(['king',98000])
file.seek(0)
reader=csv.reader(file)
for row in reader:
    print(row)
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to reading and writing file using r+
import csv
file=open('main.csv','r+',newline='')
reader=csv.reader(file)
for row in reader:
    print(row)
writer=csv.writer(file)
writer.writerow(['scott',6800])
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to appending and reading using a+
import csv
file=open('main.csv','a+',newline='')
writer=csv.writer(file)
writer.writerow(['james',7890])
file.seek(0)
reader=csv.reader(file)
for row in reader:
    print(row)
file.close()

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to store employee number,employee name,salary and annual salary by taking user input in csv filehandling
import csv
# Open the csv file for writing
with open('emp1.csv','w',newline='') as f:
    w=csv.writer(f)
    # write the header
    w.writerow(['eno','ename','sal','annual_salary'])
    # get the number of employees
    num=int(input('Enter the number of employees:'))
    # loop to get employee details and write them to the csv
    for i in range(num):
        eno=int(input('Enter the employee code:'))
        ename=input('Enter the name of employee:')
        sal=int(input('Enter the salary of the employee:'))
        annual_salary=sal*12
        # write the employee data
        w.writerow([eno,ename,sal,annual_salary])
    print('Successfull')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP example for dictionary
import csv
# sample employee details
employees=[
    {'eno':1,'ename':'Alice','sal':5000,'dno':101},
    {'eno':2,'ename':'Amar','sal':6000,'dno':102},
    {'eno':3,'ename':'Anu','sal':6500,'dno':103}
]
# open  csv file for wwrriting
with open('emp2.csv','w',newline='') as f:
    w=csv.writer(f)
    # write the header
    w.writerow(['eno','ename','sal','dno','annual_sal'])
    # loop through the predefined employee data and write it to the csv
    for emp in employees:
        annual_sal=emp['sal']*12
        w.writerow([emp['eno'],emp['ename'],emp['sal'],emp['dno'],annual_sal])
    print('Successfull')

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to read the file using with statement
import csv
with open('emp2.csv','r') as file:
    rows=csv.reader(file)
    for row in rows:
        print(row)    

#-----------------------------------------------------------------------------------------------------------------------------#

# WAP to store students information using nested dictionary
import csv         
# Nested dictionary data
students={
    's001':{'name':'smith','age':20,'subject':'python'},
    's002':{'name':'scott','age':25,'subject':'java'},
    's001':{'name':'Arun','age':28,'subject':'SQl'}
}
filename='Students_data.csv'
# writing to csv
with open(filename,'w',newline='') as f:
    w=csv.writer(f)
    # write the header
    w.writerow(['sid','name','age','subject'])
    # loop through the nested dictionary
    for sid,info in students.items():
        w.writerow([
            sid,
            info['name'],
            info['age'],
            info['subject']
        ])
    print(f'Successfull:data written to {filename}')        

#-----------------------------------------------------------------------------------------------------------------------------#
