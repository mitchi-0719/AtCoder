# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
inf = float("inf")
# fmt: on


def dfs(n, s, cur, st, d):
    if d[cur]:
        return False

    if s[cur] == "1":
        d[cur] = True
        return False

    if cur == 2**n - 1:
        return True

    for i in st:
        st.remove(i)
        if dfs(n, s, cur + (2**i), st, d):
            return True
        st.add(i)

    d[cur] = True
    return False


def solve():
    n = I()
    s = "0" + S()
    d = defaultdict(bool)

    print(yes_no(dfs(n, s, 0, set([i for i in range(n)]), d)))


t = I()
for _ in range(t):
    solve()
