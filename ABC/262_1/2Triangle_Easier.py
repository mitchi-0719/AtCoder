#notClear

n, m = map(int, input().split())
u = [0] * m
v = [0] * m

for i in range(m):
    u[i], v[i] = map(int, input().split())

cnt = 0

for i in range(m):
    if v[i] == n:
        continue
    else:

        j = 0
        while(j < m and u[j] != v[i]):
            j += 1
        if j != m:
            for l in range(m):
                if v[l] == v[j] and u[i] == u[l]:
                    cnt += 1
print(cnt)