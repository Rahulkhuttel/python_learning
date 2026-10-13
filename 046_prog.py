a=int(input('Enter a number: '))#123
n=a

i=0
while a>0:
    b=a%10
    i=(i*10)+b
    a=a//10

if i==n:
    print(f'{n} is palindrome number')
else:
    print(f'{n} is not palindrome number')

