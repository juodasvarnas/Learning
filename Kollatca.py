n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
        count += 1
    elif n % 2 == 1:
        n = 3 * n + 1
        count += 1
    elif count == 1:
        break
print(count)
