def li(numbers):
    total=0
    product=1
    for i in numbers:
        if i%2==0:
            product=product*i
        elif i%2==1:
            total=total+i
    print(f'product is:{product} and total is:{total}')
(li([1,2,3,4,5,6,7,8,9]))                             

