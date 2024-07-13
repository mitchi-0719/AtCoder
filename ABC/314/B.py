n = int(input())
c = []
a = []

for _ in range(n):
    c.append(int(input()))
    a.append(list(map(int, input().split())))

x = int(input())

hit = []
hit_cnt = []

for i in range(n):
    if x in a[i]:
        hit.append(i)
        hit_cnt.append(c[i])

if len(hit) != 0:
    m = min(hit_cnt)
    print(hit_cnt.count(m))
    ans = []
    for i in range(len(hit)):
        if hit_cnt[i] == m:
            ans.append(hit[i] + 1)

    print(*sorted(ans))
else:
    print(0)
    print()
