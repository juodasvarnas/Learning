"""Найти сумму каждой из строк. Вывести максимальное значение строки и её индекс"""
n, m = map(int, input().split())
a = []
s = []
summer = 0
for i in range(n):
    b = []
    for j in range(i):
        b.append(j)
    a.append(list(map(int, input().split())))
for i in range(n):
    summer = 0
    for j in range(m):
        summer += a[i][j]
    s.append(summer)
print(max(s))
print(s.index(max(s)))
