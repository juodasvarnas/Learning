n, m = map(int, input().split())
a = []
k = 0
for i in range(n):
    a.append(input())
b = [[False] * m for i in range(n)]
for i in range(n):
    if 'S' not in a[i]:
        for j in range(m):
            b[i][j] = True
for j in range(m):
    is_find = False
    for i in range(n):
        if a[i][j] == 'S':
            is_find = True
            break
    if not is_find:
        for i in range(n):
            b[i][j] = True
count = 0
for row in b:
    count += row.count(True)
print(count)

"""
Дан прямоугольный торт, который имеет вид таблицы размером r × c. Каждая ячейка таблицы содержит либо гадкую клубничку, либо является пустой. Например, торт размера 3 × 4 может выглядеть так:



Тортминатор намерен съесть этот торт! Каждый раз, когда он ест, он выбирает строку или столбец, не содержащие гадкой клубнички, а содержащие по крайней мере одну несъеденную ячейку торта. Затем Тортминатор поедает все выбранные им ячейки торта. Тортминатор может есть сколько угодно раз.

Пожалуйста, выведите максимальное количество ячеек, которые может съесть Тортминатор.

Входные данные

Первая строка содержит два целых числа r и c (2 ≤ r, c ≤ 10), обозначающих количество строк и количество столбцов в торте. Следующие r строк содержат по c символов — j-ый символ i-ой строки обозначает содержимое ячейки в строке i и столбце j, и имеет одно из следующих значений:

символ '.' обозначает ячейку торта без гадкой клубнички;
символ 'S' обозначает ячейку торта с гадкой клубничкой.
Выходные данные

Выведите максимальное количество ячеек торта, которые может съесть тортминатор.

Разбор задачи Youtube Patreon Boosty

Sample Input:

3 4
S...
....
..S.
Sample Output:

8
"""