"""Вывод списка матрицы снизу вверх справа налево"""
n = int(input())
a = []
for i in range(n):
    b = []
    for j in range(i):
        b.append(j)
    a.append(list(map(int, input().split())))
for j in range(n - 1, -1, -1):
    for i in range(n):
        print(a[i][j], end=' ')
    print()
