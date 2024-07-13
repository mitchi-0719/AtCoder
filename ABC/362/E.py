from collections import defaultdict


def dfs(d, diffs, dist, length, n, now, diff):
    if dist > length:
        return 0

    cnt = 0
    s = 0 if len(now) == 0 else now[-1] + 1
    for i in range(s, n):
        if d[now + (i,)] == -1:
            continue

        if len(now) == 1 or diffs[now[0]][now[1]] == diffs[now[1]][i]:
            cnt += dfs(d, diffs, dist + 1, n, now + (i,)) + 1

    return cnt


mod = 998244353

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
diffs = []

for i in range(n - 1):
    tmp = [None] * (i + 1)
    for j in range(i + 1, n):
        tmp.append(a[j] - a[i])
    diffs.append(tmp)

print(diffs)
for _ in range(n - 1):
    print(dfs(d, diffs, i, 0, n, tuple()) % mod)
