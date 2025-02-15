n, m = map(int, input().split())
edge = []

cnt = 0
for i in range(m):
    u, v = map(int, input().split())
    if u == v:
        cnt += 1
    else:
        if u < v:
            edge.append((u, v))
        else:
            edge.append((v, u))

edge.sort()

before = ()
for e in edge:
    if before == e:
        cnt += 1
    else:
        before = e

print(cnt)
