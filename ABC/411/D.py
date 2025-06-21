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
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

n, q = LI()
pc = [[0, [[]]] for _ in range(n)]
pc_i = [0] * n
server = [[None, []]]
server_i = 0

for _ in range(q):
    query = LS()
    i = int(query[0])
    if i == 1:
        pc[int(query[1]) - 1][0] = server_i
        pc[int(query[1]) - 1][1][pc_i[int(query[1]) - 1]] = []
    elif i == 2:
        _, p, s = query
        pc[int(p) - 1][1][pc_i[int(query[1]) - 1]].append(s)
    else:
        server.append(
            [
                pc[int(query[1]) - 1][0],
                pc[int(query[1]) - 1][1][pc_i[int(query[1]) - 1]],
            ]
        )
        pc_i[int(query[1]) - 1] += 1
        pc[int(query[1]) - 1][1].append([])
        server_i += 1

ans = ["".join(server[-1][1])]
si = server[-1][0]

while True:
    if si != None:
        ans.append("".join(server[si][1]))
        si = server[si][0]
    else:
        break


print("".join(ans[::-1]))
