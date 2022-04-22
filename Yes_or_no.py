n = int(input())
i = 1
a = []
s = 0
while i*i <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
            s = s + i
    i += i
a.sort()
print(sum(a))
"""if len(a) == 1:
    print('No')
elif len(a) <= 2:
    print('Yes')
else:
    print('No')"""

