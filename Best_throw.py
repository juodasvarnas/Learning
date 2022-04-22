"""В метании молота состязается n спортcменов. Каждый из них сделал m бросков.
Победителем соревнований объявляется тот спортсмен, у которого максимален наилучший результат по
всем броскам. Таким образом, программа должна найти значение максимального элемента в данном массиве,
а также его индексы (то есть номер спортсмена и номер попытки)."""
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
max_score = 0
max_summa = 0
max_index = 0
for i in range(n):
    summer = 0
    s = 0
    for j in range(m):
        s += a[i][j]
        if a[i][j] > summer:
            summer = a[i][j]
    if summer > max_score:
        max_score = summer
        max_summa = s
        max_index = i
    elif summer == max_score and s > max_summa:
        max_score = summer
        max_summa = s
        max_index = i
print(max_score, max_summa, max_index)
