s = input()
t = input()

check = True
if len(s) > len(t):
    check = False
else:
    for i in range(len(s)):
        if s[i] != t[i]:
            check = False
            break
if check:
    print("Yes")
else:
    print("No")