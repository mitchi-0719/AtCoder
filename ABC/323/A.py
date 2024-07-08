s = input()
for i in range(1, len(s) + 1, 2):
    if s[i] != "0":
        print("No")
        exit()

print("Yes")
