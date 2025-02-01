n, q = map(int, input().split())
su = []
hato = []
for i in range(n + 1):
    hato.append(i)
    su.append(1)
cnt = 0

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        _, p, h = query
        if su[h] == 1:
            cnt += 1

        if su[hato[p]] == 2:
            cnt -= 1

        su[hato[p]] -= 1
        su[h] += 1
        hato[p] = h
    else:
        print(cnt)
