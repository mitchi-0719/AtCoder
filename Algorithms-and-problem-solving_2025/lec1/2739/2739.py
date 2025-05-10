n, m, t = map(int, input().split())
a = list(map(int, input().split()))

ans = a[0] - m

for i in range(n - 1):
    if a[i + 1] - a[i] > 2 * m:
        ans += a[i + 1] - a[i] - 2 * m

ans += max(0, t - a[-1] - m)

print(ans)
