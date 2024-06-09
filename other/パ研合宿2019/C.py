n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(m - 1):
    for j in range(i + 1, m):
        if i == j:
            continue
        s = 0
        for k in range(n):
            s += max(a[k][i], a[k][j])
        ans = max(ans, s)

print(ans)
