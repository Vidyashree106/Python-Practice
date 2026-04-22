# dictionary method
# get method
# syntax: variablename.get(key)
data={'ename':'smith','sal':98000}
data.get('sal')     # 98000

#-----------------------------------------------------------------------------------------------------------------------------#

# update method
# syntax: variablename.update(key:valuepairs)
data={'ename':'smith','sal':98000}
data.update({'sal':90000})
print(data)     # {'ename': 'smith', 'sal': 90000}

#-----------------------------------------------------------------------------------------------------------------------------#

# syntax: variablename.update(key:valuepairs)
data={'ename':'smith','sal':98000}
data.update({'job':'analyst'})
print(data)     # {'ename': 'smith', 'sal': 98000, 'job': 'analyst'}

#-----------------------------------------------------------------------------------------------------------------------------#

# items method
# syntax: varaiablename.items()
data={'ename': 'smith', 'sal': 98000}
print(data.items())     # dict_items([('ename', 'smith'), ('sal', 98000)])

#-----------------------------------------------------------------------------------------------------------------------------#

# keys method
data={'ename': 'smith', 'sal': 98000}
print(data.keys())          # dict_keys(['ename', 'sal'])

#-----------------------------------------------------------------------------------------------------------------------------#

# values method
data={'ename': 'smith', 'sal': 98000}
print(data.values())        # dict_values(['smith', 98000])

#-----------------------------------------------------------------------------------------------------------------------------#

# Match case statement
# syntax: match variable:
            # case value 1:
            #     code Block
            # case value 2:
            #     code block
            # case value 3:
            #     code block
            # case_:
            #     default case(like else)

num=int(input('Enter the number:'))
match num:
    case 1:
        print('you enterd one')     # you enterd one
    case 2:
        print('you enterd two')     # you enterd two
    case _:
        print("another number")     # 3,another number

#-----------------------------------------------------------------------------------------------------------------------------#

days=int(input('Enter the day from 1 to 7:'))
match days:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursady')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Day number is invalid')                                    

#-----------------------------------------------------------------------------------------------------------------------------#

balance=97000
while True:
    print('\n----Bank Menu----')
    print('1.Check balance')
    print('2.Deposite')
    print('3.Withdraw amount')
    print("4.exit")

    choice=eval(input('Enter the choice from 1 to 4:'))
    match choice:
        case 1:
            print(f'Balance is:{balance}')
        case 2:
            amount=float(input('Enter the amount:'))
            if amount>0:
                balance=balance+amount
                print(f'Rs {amount} deposited to account')
                print(f'The updated balance is:{balance}')
            else:
                print(f'Amount should be greater than zero')
        case 3:
            amount=float(input('Enter the amount to withdraw:'))
            if amount<=balance and amount>0:
                balance=balance-amount
                print(f'Rs {amount} withdrawn from account')
                print(f'The updated balance is:{balance}')
            else:
                print(f'Insufficient balance')
        case 4:
            print('Thanks for using Banking,Good bye!')
            break
        case _:
            print('Invalid choice choose from 1 to 4')   
        
#-----------------------------------------------------------------------------------------------------------------------------#



