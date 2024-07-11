def dfs(g, visited, dist, start, n):
    if dist == n - 1:
        return True

    visited[start] = True
    judge = False
    for i in g[start]:
        if visited[i]:
            continue

        judge = judge or dfs(g, [*visited], dist + 1, i, n)

    return judge


n, m = map(int, input().split())
s = [input() for _ in range(n)]
g = [set() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        cnt = 0
        for s1, s2 in zip(s[i], s[j]):
            if s1 != s2:
                cnt += 1
        if cnt == 1:
            g[i].add(j)
            g[j].add(i)

for i in range(n):
    if dfs(g, [False] * n, 0, i, n):
        print("Yes")
        exit()

print("No")
