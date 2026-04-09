# Nested if statement
# Syntax:  if condition:
            #     if condition: 
            #         # true statement block
            #     else:                         
            #         # false statement block
            # else:
            #     # false statement block

# WAP to check the given number is positive,negative,zero if the number is positive then check whether it is even or odd
num=97
if num>0:
    print(f'{num} is positive')
    if num%2==0:
        print(f'{num} is even')                 # 97 is positive
    else:
        print(f'{num} is odd')                  # 97 is odd
elif num<0:
    print(f'{num} is negative')             # -45 is negative
else:
    print('Zero')                           # 0 is zero

# WAP to check the given year is leap year or not if it is leap year check the year is even or odd
year=2024
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f'{year} is a leap year')
    if year%2==0:
        print(f'{year} is an even year')                 # 2024 is a leap year and 2024 is an even year
    else:
        print(f'{year} is an odd year') 

# WAP to find the second largest number among three numbers
a=10
b=20
c=15
if a>b and a>c:
    if b>c:
        print(f'{b} is the second largest number')     # 20 is the second largest number
    else:
        print(f'{c} is the second largest number')
elif b>a and b>c:
    if a>c:
        print(f'{a} is the second largest number')     # 10 is the second largest number
    else:
        print(f'{c} is the second largest number')
else:    
    if a>b:
        print(f'{a} is the second largest number')     # 15 is the second largest number    
    else:
        print(f'{b} is the second largest number')

# WAP to find third lowest number among three numbers
a,b,c=10,15,89
if a<b:
    if b<c:
        print(f'{b} is the third lowest number')     # 89 is the third lowest number
    elif a<c:
        print(f'{a} is the third lowest number')     # 10 is the third lowest number
    else:
        print(f'{c} is the third lowest number')     # 15 is the third lowest number
elif a<c:
    print(f'{a} is the third lowest number')         # 89 is the third lowest number
elif b<c:
    print(f'{b} is the third lowest number')         # 15 is the third lowest number
else:   
    print(f'{c} is the third lowest number')         # 10 is the third lowest number

# WAP to perform check balance,deposite and withdraw and exit operation using nested if statement
balance=1000
print('Welcome to the ATM')
print('\nATM Menu')
print('1. Check balance')
print('2. Deposit')
print('3. Withdraw')
print('4. Exit')    

choice=int(input('\nEnter your choice: '))
if choice==1:
    print(f'Your current balance is: {balance}')
elif choice==2:
    deposite=float(input('Enter the amount to deposit: '))
    if deposite>0:
        balance=balance+deposite
        print(f'\n {deposite} deposited successfully.\n New balance:{balance}')
    else:
        print(f'Your new balance is: {balance}')
elif choice==3:
    withdraw=float(input('Enter the amount to withdraw: '))
    if withdraw<=balance:
        balance=balance-withdraw
        print(f'{withdraw} withdrawn successfully.\n New balance: {balance}')
    else:
        print('Insufficient balance')
elif choice==4:
    print('\nThank you for using the ATM!')
else:
    print('Invalid choice! Please enter a valid choice.')


# WAP to book a movei ticket in Book myshow
# conditions: It should asl theater name,it should display movei available,it should display  ticket price, it should ask do you want to confirm booking    
print('Welcome to Book My Show')
theater_name=input('Enter the theater name (PVR, INOX):')
if theater_name=='PVR' or theater_name=='INOX':
    if theater_name=='PVR':
        print('\n Movies available at PVR:')
        movie1='Avatar:The way of water'
        movie2='The batsman'
        ticket_price1=800
        ticket_price2=850
    else:
        print('\n Movies available at INOX:')
        movie1='Mission impossible:fallout'
        movie2='Jurassic world: dominion'
        ticket_price1=900
        ticket_price2=950
    print(f'{movie1}')
    print(f'{movie2}')
    movie_choice=input('\n Enter the movie number your chosen movie (1/2):')
    if movie_choice == '1' or movie_choice=='2':
        if movie_choice=='1':
            selected_movie=movie1
            ticket_price=ticket_price1
        else:
            selected_movie=movie2
            ticket_price=ticket_price2
        print(f'\n You have selected : {selected_movie}')
        print(f'Ticket price:RS-{ticket_price}')
        confirmation=input('\nDo you want to confirm the booking? (yes/no):')
        if confirmation=='yes':
            print(f'\n Your Ticket for {selected_movie} has been booked successfully!')
        else:
            print(f'\n Ticket booking has been cancelled.')
    else:
        print(f'\n Invalid movie choice! Please select a valid movie number.')
else:
    print(f'\n Sorry Theater name is not available.')


    