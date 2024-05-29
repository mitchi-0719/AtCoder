n = int(input())
a = [0] + list(map(int, input().split()))

g = [[] for _ in range(n)]

ans = [0] * n

for i in range(1, n):
    g[a[i] - 1].append(i + 1)

for i in range(1, n + 1):
    if len(g[-i]) != 0:
        ans[-i] += len(g[-i])
        for c in g[-i]:
            ans[-i] += ans[c - 1]

print(*ans)
