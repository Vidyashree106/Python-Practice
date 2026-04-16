# jumping statements : break, continue, pass

# break : it is used to exit from the loop when a condition is satisfied
# Example:
for num in range(1,11):
    if num==5:
        break
    print(num,end=' ')          # 1 2 3 4

#-----------------------------------------------------------------------------------------------------------------------------#

# continue : it is used to skip the current iteration when a condition is satisfied
# Example:
for num in range(1,11):
    if num==5:
        continue
    print(num,end=' ')          # 1 2 3 4 6 7 8 9 10    

#-----------------------------------------------------------------------------------------------------------------------------#

# pass : it is used to do nothing when a condition is satisfied
# Example:
for num in range(1,11):
    if num==5:
        pass
    print(num,end=' ')          # 1 2 3 4 5 6 7 8 9 10
    
#-----------------------------------------------------------------------------------------------------------------------------#
