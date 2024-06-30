import bisect

n, t = map(int, input().split())
s = list(input())
x = list(map(int, input().split()))
xm = sorted([x[i] for i in range(n) if s[i] == "0"])
xp = sorted([x[i] for i in range(n) if s[i] == "1"])

ans = 0
for i in range(n):
    if s[i] == "0":
        st = bisect.bisect(xp, x[i])
        en = bisect.bisect_left(xp, x[i] - t * 2)
        ans += abs(st - en)
    else:
        st = bisect.bisect(xm, x[i])
        en = bisect.bisect_right(xm, x[i] + t * 2)
        ans += abs(st - en)

print(ans // 2)
