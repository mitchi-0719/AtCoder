n = int(input())
s = []

m = 0
for i in range(n):
    s.append(input())
    m = max(m, len(s[i]))


for i in range(m):
    cnt = 0
    for j in range(n - 1, -1, -1):
        if len(s[j]) > i:
            print("*" * cnt, end="")
            print(s[j][i], end="")
            cnt = 0
        else:
            cnt += 1
    print()
