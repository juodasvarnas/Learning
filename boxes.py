# Ване на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду.
# Ваня хочет построить пирамиду следующим образом: на верхушке пирамиды должен находиться 1 кубик,
# на втором уровне — 1 + 2 = 3 кубика, на третьем — 1 + 2 + 3 = 6 кубиков,
# и так далее. Таким образом, на i-м уровне пирамиды должно располагаться
# 1 + 2 +...+ (i - 1) + i  кубиков.
n = int(input())
count = 0
h = 0
while h < n:
    count += 1
    h = h + count
    n = n - h
if n < 0:
    print(count - 1)
else:
    print(count)
