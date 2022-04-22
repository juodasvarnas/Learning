a = int(input())
b = int(input())
c = a - 1
while c < b:
    c = c + 1
    if c == 777:
        break
    if c % 2 == 0 or c % 3 == 0:
        continue
    print(c)
