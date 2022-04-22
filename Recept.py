n = int(input())
recept = []
for i in range(n):
    s = input()
    if s.find('соль') == -1:
        recept.append(s)
print(*recept, sep=', ')

