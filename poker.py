r = int(input())
sm = 0
sk = 0
for i in range(r):
    m, k = map(int, input().split())
    sm += m
    sk += k
if sm > sk:
    print('Mishka')
elif sk > sm:
    print('Chris')
else:
    print('Friendship is magic!^^')
