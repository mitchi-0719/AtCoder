n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

ans = float("inf")
for i in range(n - (n - k) + 1):
    ans = min(ans, a[i + (n - k) - 1] - a[i])

print(ans)
