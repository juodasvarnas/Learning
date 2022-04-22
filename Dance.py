"""number = 73408
m = 0
s = 0
while number > 0:
    last_digit = number % 10
    s = s + last_digit
    if last_digit > m:
        m = last_digit
    number = number // 10
print(s + m)"""
a = int(input())
s = 0
pr = 1
minimum = 9
maximum = 0
count = 0
while a > 0:
    last_digit = a % 2
    print(last_digit)
    #if last_digit == 7:
    #   count += 1
    #pr = pr * last_digit
    #s = s + last_digit
    #print(last_digit)
    """if last_digit < minimum:
        minimum = last_digit
    if last_digit > maximum:
        maximum = last_digit"""
    a = a // 2

