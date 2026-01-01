# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
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

s = S()


def solve(S):
    N = len(S)
    s = ""
    d = defaultdict(int)

    i = 0
    # 文字列の終わりまでループ
    while 1:
        if i == N:
            return d

        if S[i].isalpha():
            # アルファベットならば、それまでに集計した数値を辞書に加算
            n = int(s if s != "" else 1)
            d[S[i]] += n
            i += 1
            s = ""
        elif S[i].isdecimal():
            # 数値ならば、集計
            s += S[i]
            i += 1
        else:
            # 開カッコならば
            _i = i

            # 対応する閉じカッコを探索
            # 開カッコを+1、閉じカッコを-1として加算していったときに、数値が0になったらその場所が対応する閉じカッコ
            sc = 0
            while 1:
                if S[_i] == "(":
                    sc += 1
                if S[_i] == ")":
                    sc -= 1
                if sc == 0:
                    break

                _i += 1

            # カッコの範囲がわかったらその範囲内をsliceして再帰。その範囲の辞書を得る。
            _d = solve(S[i + 1 : _i])
            i = _i + 1
            n = int(s if s != "" else 1)

            # 得た辞書の各文字の個数をそれまでに集計していた数値倍して辞書に加算
            for k, v in _d.items():
                d[k] += v * n
            s = ""

    return d


d = solve(s)

for i in range(26):
    c = chr(ord("a") + i)
    print(c, d[c])

"""
数値を集計し、アルファベットが出てきたらその数値倍した値を辞書に加算
    (数値が1で省略されているときは空文字列("")のため、それを判定して1倍としてる)
カッコが出てきたらそのカッコの終わりを探索して、カッコ内の文字列をsliceして再帰に入る
再帰が終わったら、その内部での辞書が得られるので、得た辞書の各値をそれまでに集計してた数値倍して、辞書に加算
"""
