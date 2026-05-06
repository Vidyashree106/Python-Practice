balance=98000
withdraw=int(input('Enter the amount to withdraw:'))
try:
    if withdraw>balance:
        raise Exception(f'amount should be less than {balance}')
    balance=balance-withdraw
    print(f'{withdraw} amount is debited')
    print(f'updated balance is {balance}')
except Exception as e:
    print(f'error:{e}')
    
#-----------------------------------------------------------------------------------------------------------------------------#
    