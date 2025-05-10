n = int(input())
s = [input() for _ in range(n)]

ac = 0
for si in s:
    if si == "A":
        ac += 1
    else:
        ac -= 1

    if ac < 0:
        print("NO")
        exit()

if ac == 0:
    print("YES")
else:
    print("NO")
