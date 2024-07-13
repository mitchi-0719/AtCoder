n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
ans = []

s = 0
for l, r in lr:
    s += l
    ans.append(l)

if s > 0:
    print("No")
    exit()

if s == 0:
    print("Yes")
    print(*ans)
    exit()

s = abs(s)
for i in range(n):
    l, r = lr[i]
    if r - l >= s:
        ans[i] = l + s
        print("Yes")
        print(*ans)
        exit()
    else:
        ans[i] = r
        s -= r - l


print("No")
