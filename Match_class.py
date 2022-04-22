class Team:
    def __init__(self, h, q):
        self.home = h
        self.no_home = q


n = int(input())
k = 0
command = []
for i in range(n):
    home, no_home = map(int, input().split())
    command.append(Team(home, no_home))
for i in range(n - 1):
    for j in range(i + 1, n):
        if command[i].home == command[j].no_home:
            k += 1
        if command[i].no_home == command[j].home:
            k += 1
print(k)
