try:
    a=int(input('Enter number: '))
    b=int(input('Enter number: '))

    print(f'Division of {a} by {b} is {a/b}')
except ValueError:
    print('Thier is some error in value')
except ZeroDivisionError:
    print('We cannot divide a number by 0')