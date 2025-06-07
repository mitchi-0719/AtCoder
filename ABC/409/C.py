# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

n, l = LI()
d = LI()

c = defaultdict(list)
cur = 0
c[0].append(0)

for i, di in enumerate(d):
    cur = (cur + di) % l
    c[cur].append(i + 1)

if l % 3 != 0:
    print(0)
    exit()

diff = l // 3
cur_p = 0
ans = 0
for i in range(diff):
    ans += len(c[i]) * len(c[i + diff]) * len(c[i + diff * 2])

print(ans)
