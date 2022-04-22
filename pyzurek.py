n = int(input())
a = list(map(int, input().split()))
c = 0
if n == len(a):
    for sum in range(n - 1):
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                c += 1
                a[i], a[i + 1] = a[i + 1], a[i]
for i in a:
    print(i, end=" ")
