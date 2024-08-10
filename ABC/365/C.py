from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
a_sort = sorted(list(set(a)), reverse=True)
set_n = len(set(a))
s = sum(a)
d = defaultdict(int)
inf = "infinite"

if s <= m:
    print(inf)
    exit()

for ai in a:
    d[ai] += 1


for i in range(1, set_n):
    sub = (a_sort[i - 1] - a_sort[i]) * d[a_sort[i - 1]]
    s -= sub
    if s <= m:
        tmp = sub // 4
        _tmp = 0 if tmp == 0 else (m - s) // tmp
        print(a_sort[i] + _tmp)
        exit()

print(m // n)
