s, t = input().split()
t = list(t)

for i in range(1, len(s)):
    for ti in range(i):
        if t == [s[j] for j in range(ti, len(s), i)]:
            print("Yes")
            exit()

print("No")
