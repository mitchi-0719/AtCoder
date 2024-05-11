s = input()
t = input()

i = 0
for a in s:
    while True:
        if a == t[i]:
            print(i + 1, end=" ")
            i += 1
            break
        i += 1
