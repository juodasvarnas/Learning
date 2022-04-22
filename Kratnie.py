n = int(input())
s = 0
for i in range(n):
    if i % 5 == 0 or i % 3 == 0:
        s += i
print(s)
