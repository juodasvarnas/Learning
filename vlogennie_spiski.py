n = int(input())
a = []
s = 0
for i in range(n):
    b = []
    for j in range(i):
        b.append(j)
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i == j:
            s += a[i][j]
print(s)
