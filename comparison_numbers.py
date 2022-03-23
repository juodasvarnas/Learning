a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and a == c:
    print(3)
elif b != a == c or a != b == c or c != a == b:
    print(2)
else:
    print(0)
