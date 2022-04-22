"""Вывод списка матрицы справа налево сверху вниз"""
n, m = map(int, input().split())
a = []
for i in range(n):
    b = []
    for j in range(i):
        b.append(j)
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m - 1, -1, -1):
        print(a[i][j], end=' ')
    print()
