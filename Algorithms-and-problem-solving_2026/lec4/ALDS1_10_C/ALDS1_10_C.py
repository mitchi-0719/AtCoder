# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, string, queue
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**8)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return yes if b else no
def sigma(n): (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on


N = I()

for _ in range(N):
    X = S()
    Y = S()
    n, m = len(X), len(Y)
    # 文字列X, Yごとに1行増やしたdpテーブルを作成
    dp = [[-1 for _ in range(m + 1)] for __ in range(n + 1)]

    # 両方から0文字取ったときの共通部分列長は0なので0で初期化
    for i in range(n + 1):
        dp[i][0] = 0

    for j in range(m + 1):
        dp[0][j] = 0

    # 文字列Xのi文字目と一致する文字列Yの文字が存在するか探索し、
    # 存在する: i文字目&j文字目の1ツ前の文字である、i-1, j-1の段階での一致数を加算する
    # 存在しない: 現在の文字を無視し、その直前（上or左）のmaxを取る
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[-1][-1])
