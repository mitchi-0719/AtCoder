n, m = map(int, input().split())

g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


cnt = 0
for i in range(n + 1):
    g[i] = sorted(g[i])
    if len(g[i]) == 1 and g[i][0] < i or len(g[i]) >= 2 and g[i][0] < i and g[i][1] > i:
        cnt += 1
print(cnt)
