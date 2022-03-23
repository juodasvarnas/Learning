a = input()
b = input()
a = a.lower()
b = b.lower()
if 1 <= len(a) <= 100 and 1 <= len(b) <= 100 and len(a) == len(b):
    if a < b:
        print(-1)
    elif a > b:
        print(1)
    else:
        print(0)
else:
    print('Wroooooong')


