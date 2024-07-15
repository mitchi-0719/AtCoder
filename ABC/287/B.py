n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = set([input() for _ in range(m)])

ans = 0
for si in s:
    p = si[-3:]
    ans += 1 if p in t else 0

print(ans)
