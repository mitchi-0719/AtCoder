abcde = list(map(int, input().split()))

ans = []
for i in range(1, 32):
    s = 0
    st = ""
    for j in range(5):
        if (i >> j) % 2 == 1:
            s += abcde[j]
            st += chr(ord("A") + j)
    ans.append([s, st])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))

for ai in ans:
    print(ai[1])
