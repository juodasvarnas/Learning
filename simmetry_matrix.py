"""Проверьте, является ли двумерный массив симметричным относительно главной диагонали.
Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний."""
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
s = 0
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            s += 1
print('Yes' if s == 0 else 'No')
