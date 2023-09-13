#正解

s = input()

t = "oxx"

if len(s) == 1:
    print("Yes")
    exit()
elif len(s) == 2:
    for i in range(3):
        chk = t[i] + t[(i + 1) % 3]
        if chk == s:
            print("Yes")
            exit()
else:
    for i in range(3):
        chk = ""
        for j in range(len(s)):
            chk += t[(j + i) % 3]
        if chk == s:
            print("Yes")
            exit()
print("No")