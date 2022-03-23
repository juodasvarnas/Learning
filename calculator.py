a = float(input())
b = float(input())
z = input()
if z == '/':
    if b == 0:
        print('Неизвестно')
    else:
        print(a / b)
elif z == '+':
    print(a + b)
elif z == '-':
    print(a - b)
elif z == '*':
    print(a * b)
else:
    print('Неизвестно')

