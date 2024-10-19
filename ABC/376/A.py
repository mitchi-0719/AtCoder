n, c = map(int, input().split())
t = list(map(int, input().split()))

before = t[0]
ans = 1
for ti in t[1:]:
    if ti - before >= c:
        ans += 1
        before = ti

print(ans)
