a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    if a[i] > 0:
        b.append(a[i])
if len(b) == 0:
    print('Empty')
else:
    print(min(b))
