year = int(input('Напишите год: '))

if year % 4 != 0:
    print('Год не является високосный.')

elif year % 100 == 0:
    if year % 400 == 0:
        print('Високосный год.')
    else:
        print('Год не является високосный.')
else:
    print('Високосный год .')