a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')
    s += i**3
print('Сумма всех кубов числа = ', s)
