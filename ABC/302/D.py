import bisect

n, m, d = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
ans = -1


for ai in a:
    i = bisect.bisect(b, ai + d)
    if abs(ai - b[i - 1]) <= d:
        ans = max(ans, ai + b[i - 1])

print(ans)
