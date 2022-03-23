a, b, c = map(int, input().split())
if c < a > b:
    if c > b:
        print(a - b)
    else:
        print(a - c)
elif a < b > c:
    if a > c:
        print(b - c)
    else:
        print(b - a)
elif a < c > b:
    if a > b:
        print(c - b)
    else:
        print(c - a)
else:
    print('Wrong input, please try again')
