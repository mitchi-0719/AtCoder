s = input()
ox = "oxx"

d = 0
if s[0] == "x":
    if len(s) >= 2 and s[1] == "x":
        d = 1
    elif len(s) >= 2 and s[1] == "o":
        d = 2
    else:
        print("Yes")
        exit()

for i in range(len(s)):
    if s[i] != ox[(i + d) % 3]:
        print("No")
        exit()

print("Yes")
