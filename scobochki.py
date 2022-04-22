a = input()
s = []
is_good = True
for i in a:
    if i in '{[(':
        s.append(i)
    elif i in '}])':
        if not s:
            is_good = False
            break
        st = s.pop()
        if st == '(' and i == ')':
            continue
        if st == '{' and i == '}':
            continue
        if st == '[' and i == ']':
            continue
        is_good = False
        break
if is_good and len(s) == 0:
    print('YES')
else:
    print('NO')
