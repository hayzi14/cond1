a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))


if (a > b and a < c) or (a > c and a < b):
       print(a)
elif (b > a and b < c) or (b > c and b < a):
       print(b)
elif (c > a and c < b) or (c > b and c < a):
       print(c)
elif a == b or a == c or b == c :
       print('error')   