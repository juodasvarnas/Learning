"""Слева направо снизу вверх"""
n, m = map(int, input().split())
a = []
for i in range(n):
    b = []
    for j in range(i):
        b.append(j)
    a.append(list(map(int, input().split())))
for i in range(n - 1, -1, -1):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
