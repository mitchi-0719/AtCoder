# ワーシャル–フロイド法


def warshall_floyd(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


n, m = map(int, input().split())
d = [[float("inf") for _ in range(n)] for __ in range(n)]

for _ in range(m):
    v1, v2, c = map(int, input().split())
    d[v1][v2] = c

for i in range(n):
    d[i][i] = 0

warshall_floyd(d, n)

ans = 0
for i in range(n):
    for j in range(n):
        ans += d[i][j]

print(ans)
