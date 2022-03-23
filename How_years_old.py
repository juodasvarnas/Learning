a = int(input())
if 0 >= a < 2:
    print('Младенец')
elif 2 == a or a < 4:
    print('Малыш')
elif 4 == a or a < 12:
    print('Ребенок')
elif 12 == a or a < 19:
    print('Подросток')
elif 19 == a or a < 65:
    print('Взрослый человек')
elif a >= 65:
    print('Пожилой человек')
