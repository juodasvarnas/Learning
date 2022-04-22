n = int(input())
a = [[0] * n for i in range(n)]
k, q = 1, 0
a[n // 2][n // 2] = n * n
for i in range(n // 2):
    for j in range(n - q):
        a[i][j + i] = k
        k += 1
    for j in range(i + 1, n - i):
        a[j][-i - 1] = k
        k += 1
    for j in range(i + 1, n - i):
        a[-i - 1][-j - 1] = k
        k += 1
    for j in range(i + 1, n - (i + 1)):
        a[-j - 1][i] = k
        k += 1
    q += 2
for i in a:
    print(i)
"""
Абсоютно не понятно для понимания,Изучить в обязательном порядке!!!
"""
