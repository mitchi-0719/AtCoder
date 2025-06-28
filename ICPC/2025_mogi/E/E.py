import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)


def get_var(i, s):
    if e[i] != "if":
        return

    s.add(e[i + 1])
    get_var(i + 3, s)
    get_var(i + 5, s)


def solve(i, v, d, tf, l):
    if e[i] != "if":
        return int(e[i]) * (l - len(v) + 1), i

    e1, e2 = 0, 0
    var = e[i + 1]
    d[var] += 1
    v.add(var)

    flag = tf[var] == 0
    if flag:
        tf[var] = 1
    e1, end = solve(i + 3, v, d, tf, l)
    if flag:
        tf[var] = 0

    if flag:
        tf[var] = -1
    e2, end = solve(end + 2, v, d, tf, l)
    if flag:
        tf[var] = 0

    if tf[var] == 1:
        e2 = 0
    elif tf[var] == -1:
        e1 = 0

    d[var] -= 1
    if d[var] == 0:
        tf[var] = 0
        v.remove(var)

    return e1 + e2, end


mod = 998244353
e = input().split("_")
s = set()
get_var(0, s)
d = defaultdict(int)
tf = defaultdict(int)
print(solve(0, set(), d, tf, len(s))[0] % mod)
