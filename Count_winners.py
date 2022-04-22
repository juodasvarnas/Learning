"""В метании молота состязается n спортcменов. Каждый из них сделал m бросков.
Победитель определяется по лучшему результату. Определите количество участников состязаний,
которые разделили первое место, то есть определите количество строк в массиве, которые содержат значение,
равное наибольшему."""
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
max_score = 0
x = 0
for i in range(n):
    summer = 0
    for j in range(m):
        if a[i][j] > summer:
            summer = a[i][j]
    if summer > max_score:
        max_score = summer
for i in range(n):
    for j in range(m):
        if a[i][j] == max_score:
            x += 1
            break
print(x)
