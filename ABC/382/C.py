import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

bi = [i for i in range(m)]

b, bi = zip(*sorted(zip(b, bi)))
b = list(b)
bi = list(bi)

ans = [-1 for _ in range(m)]
s = 0
e = m

for i in range(n):
    if s >= m:
        break

    idx = bisect.bisect_left(b, a[i], 0, e)
    for j in range(idx, e):
        ans[bi[j]] = i + 1
    e = idx

for i in range(m):
    print(ans[i])
