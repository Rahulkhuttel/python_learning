a=int(input('Enter a number: ')) 
n=a

i=1
count=0
while i<a:
    if a%i==0:
        count=count+(i)
    i=i+1

if count==n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')