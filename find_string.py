n = int(input())
for i in range(1, n + 1):
    s = input().lower()
    if s.find('рок') != -1:
        print(i, s.find('рок') + 1)
