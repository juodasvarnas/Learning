n, x = map(int, input().split())
k = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == x:
            k += 1
print(k)
