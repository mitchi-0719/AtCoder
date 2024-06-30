from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

d = defaultdict(int)

ans = 0
for i in range(n):
    if d[a[i]] == 0:
        d[a[i]] = w[i]
    elif d[a[i]] <= w[i]:
        ans += d[a[i]]
        d[a[i]] = w[i]
    else:
        ans += w[i]

print(ans)
