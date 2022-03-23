s, v1, v2, t1, t2 = map(int, input().split())
if 1 <= s <= 1000 and 1 <= v1 <= 1000 and 1 <= v2 <= 1000 and 1 <= t1 <= 1000 and 1 <= t2 <= 1000:
    if (s * v1 + t1*2) < (s * v2 + t2*2):
        print('First')
    elif (s * v1 + t1*2) > (s * v2 + t2*2):
        print('Second')
    else:
        print('Friendship')
else:
    print('Please write number from 1 to 1000')
