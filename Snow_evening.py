# Возьмём число. Умножим его на его же первую цифру.
# Результат умножим на первую цифру результата. И так далее.
number = int(input())
while int(str(number)[0]) != 1 and number < 1000000000:
    number = int(str(number)[0]) * number
print(number)

