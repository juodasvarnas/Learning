n, m = map(int, input().split())
count = 0
for i in range(n + 1):
    for j in range(m + 1):
        a = i**2 + j
        b = j**2 + i
        if a == n:
            if b == m:
                count += 1
print(count)
