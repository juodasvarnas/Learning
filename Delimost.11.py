a = input()
chet = []
nechet = []
for i in range(len(a)):
    if i % 2 == 0:
        chet.append(int(a[i]))
    else:
        nechet.append(int(a[i]))
if (sum(chet) - sum(nechet)) % 11 != 0:
    print('NO')
else:
    print('YES')
