from collections import defaultdict
from itertools import groupby

n = int(input())
s = list(input())

d = defaultdict(int)
for g in groupby(s):
    d[g[0]] = max(d[g[0]], len(list(g[1])))

print(sum(d.values()))
