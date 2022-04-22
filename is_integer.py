a = input()
n = []
count = 0
for i in range(len(a)):
    if a[i].isdigit():
        count += 1
        n.append(int(a[i]))
print(count, sum(n))

