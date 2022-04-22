n, m = map(int, input().split())
a = []
k = 0
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(m):
        if a[i][j] == 'C' or a[i][j] == 'M' or a[i][j] == 'Y':
            k += 1
if k > 0:
    print('#Color')
else:
    print('#Black&White')
