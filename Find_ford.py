n = input()
i = 0
while i <= len(n):
    if i == len(n):
        print('Распечатали все буквы')
        break
    elif n[i] == 'a' or n[i] == 'e':
        print('Ага! Нашлась')
        break
    else:
        print('Текущая буква:', n[i])
    i += 1
