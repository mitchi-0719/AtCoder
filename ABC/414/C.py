# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
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


def base_n(x, n):
    s = ""
    while x > 0:
        s = str(x % n) + s
        x //= n
    return s


def judge(s):
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[~i]:
            return False

    return True


a = I()
n = I()
d = int(math.log10(n) + 1)
num = [str(i) for i in range(10)]
ans = 0

for j in range(1, 10):
    if j <= n and judge(str(j)) and judge(base_n(j, a)):
        ans += j

for i in range(1, d // 2 + 1):
    for p in product(num, repeat=i):
        ps = "".join(p)
        ps_rev = int(ps[::-1])
        ps = int(ps)
        s = ps * (10**i) + ps_rev
        if len(str(s)) == i * 2 and s <= n and judge(base_n(s, a)):
            ans += s

        s_temp = ps * (10 ** (i + 1)) + ps_rev
        for j in num:
            s = s_temp + int(j) * 10**i
            if len(str(s)) == i * 2 + 1 and s <= n and judge(base_n(s, a)):
                ans += s

print(ans)
