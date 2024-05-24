from collections import defaultdict

n = int(input())
t_all = [[] for _ in range(10)]
t = []

s = []
for i in range(n):
    s.append(input())
    for j, si in enumerate(s[i]):
        t_all[int(si)].append(j)

for _t in t_all:
    if len(set(_t)) == n:
        t.append(max(_t))
    else:
        d = defaultdict(int)
        tmp = []
        for ti in _t:
            d[ti] += 1
        for k, v in d.items():
            if v == 1:
                tmp.append(k)
            else:
                tmp.append(k + 10 * (v - 1))
        t.append(max(tmp))

print(min(t))
