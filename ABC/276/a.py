s = input()

for i in range(-1, -len(s)-1, -1):
    if s[i] == "a":
        print(len(s) + i + 1)
        exit()
print(-1)