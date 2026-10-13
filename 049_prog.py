a=int(input('enter a number: '))
i=a

sum_=0
while a>0:
    n=a%10
    c=n*n*n
    sum_+=c
    a=a//10

if i==sum_:
    print(f'{i} is an armstrong number')
else:
    print(f'{i} is not an armstrong number')
