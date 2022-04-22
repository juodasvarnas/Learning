n = int(input())
k = 0
command = []
for i in range(n):
    home, no_home = map(int, input().split())
    command.append([home, no_home])
for i in range(n - 1):
    for j in range(i + 1, n):
        if command[i][0] == command[j][1]:
            k += 1
        if command[i][1] == command[j][0]:
            k += 1
print(k)
