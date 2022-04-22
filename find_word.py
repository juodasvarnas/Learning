letter = input().lower()
sentence = input().split()
for i in sentence:
    if letter in i:
        print(i)
