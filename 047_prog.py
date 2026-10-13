a=int(input('Enter a number: '))

i=1
count=0
while i<=a:
    if a%i==0:
        count+=1
    i=i+1

if count==2:
    print(f'{a} has {count} factor')
else:
    print(f'{a} has {count} factor')