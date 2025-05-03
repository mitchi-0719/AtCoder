# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on


def same_count(x, ans):
    n = len(x)
    same = 0
    for i in range(n):
        for j in range(n):
            if x[i][j] == ans[i][j]:
                same += 1

    return same


n = I()
s = [S() for _ in range(n)]
t = [S() for _ in range(n)]

sr = s
same_counts = []
for _ in range(4):
    same_counts.append(same_count(sr, t))
    sr = [list(a)[::-1] for a in zip(*sr)]

answers = []

for i in range(4):
    ans = n**2 - same_counts[i] + i
    answers.append(ans)

print(min(answers))
