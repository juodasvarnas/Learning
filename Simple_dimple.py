"""На днях Иван у себя в прихожей выложил кафель, состоящий из квадратных черных и белых плиток.
Прихожая Ивана имеет квадратную форму 4х4, вмещающую 16 плиток. Теперь Иван переживает,
что узор из плиток, который у него получился, может быть не симпатичным. С точки зрения дизайна
симпатичным узором считается тот, который не содержит в себе квадрата 2х2, состоящего из плиток одного цвета."""
a = []
k = 0
for i in range(4):
    a.append(input())
if a[2][2] == a[2-1][2] and a[2][2] == a[2-1][2-1] and a[2][2] == a[2][2-1]:
    k += 1
elif a[0][0] == a[1][1] and a[2][2] == a[3][3]:
    k += 1
if k > 0:
    print('No')
else:
    print('Yes')
