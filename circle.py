a = input().lower()
s = []
for i in a:
    s.append(a.count(i))
print(max(s))
