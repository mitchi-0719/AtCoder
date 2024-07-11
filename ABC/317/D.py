n = int(input())
x, y, z, diff = [], [], [], []
aoki = 0
takahashi = 0

for _ in range(n):
    xi, yi, zi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    z.append(zi)
    diff.append(yi - xi)

    if xi > yi:
        takahashi += zi
    else:
        aoki += zi

"""
引数メモ
dp 1: 鞍替え数
dp 2: visited
"""
dp = [[[0, set()] for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[0][i][0] = max(0, diff[i])
    dp[0][i][1].add(i)

print(dp)
print(diff)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if k in dp[i][j][1]:
                continue
