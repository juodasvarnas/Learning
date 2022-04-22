n = int(input())
s = 0
k = 0
while s <= n:
    a = int(input())
    s += a
    k += 1
print('Довольно!', s - a, k - 1, sep='\n')
