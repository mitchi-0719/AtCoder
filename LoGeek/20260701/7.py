# fmt: off
from itertools import accumulate
import sys

def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def SI(): return sys.stdin.readline().rstrip() # 文字列
# fmt: on

H, W, K = LI()
S = [list(map(int, list(SI()))) for _ in range(H)]
acc = [[0] + list(accumulate(s)) for s in S]


cnt = 0
for j1 in range(W):
    for j2 in range(j1 + 1, W + 1):

        d = {}
        c = 0
        d[0] = 1

        for i in range(H):
            c += acc[i][j2] - acc[i][j1]
            cnt += d.get(c - K, 0)
            d[c] = d.get(acc, 0) + 1

print(cnt)
