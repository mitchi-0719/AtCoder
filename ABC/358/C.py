import itertools

n, m = map(int, input().split())
s = [set() for _ in range(n)]

for i in range(n):
    li = input()
    for j in range(m):
        if li[j] == "o":
            s[i].add(j)

ans = float("inf")
for i in range(1, n + 1):
    for v in itertools.combinations(s, i):
        su = []
        for vi in v:
            su += list(vi)
        if len(set(su)) == m:
            ans = min(ans, len(v))

print(ans)
