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


def base_n(num_10, n):
    str_n = ""
    while True:
        str_n += chr(ord("a") + num_10 % n)
        num_10 = max(-1, num_10 - n)
        num_10 //= n

        if num_10 < 0:
            break

    return str_n[::-1]


n = I()
print(base_n(n - 1, 26))
