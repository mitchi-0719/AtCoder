from collections import defaultdict

n, t = map(int, input().split())
s = [0 for _ in range(n)]

ans = 1
d = defaultdict(int)
d[0] = n

for i in range(t):
    a, b = map(int, input().split())
    d[s[a - 1]] -= 1

    if d[s[a - 1]] == 0:
        ans -= 1
    if d[s[a - 1] + b] == 0:
        ans += 1

    s[a - 1] += b
    d[s[a - 1]] += 1
    print(ans)
