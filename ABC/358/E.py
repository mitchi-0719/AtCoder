from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)

frac_memo = defaultdict(int)


def frac(n):
    if frac_memo[n] != 0:
        return frac_memo[n]

    if n == 0:
        frac_memo[n] = 1
        return frac_memo[n]

    frac_memo[n] = n * frac(n - 1)
    return frac_memo[n]


p_memo = defaultdict(int)


def permutation(n, r):
    if p_memo[(n, r)] != 0:
        return p_memo[(n, r)]

    if r == 0:
        p_memo[(n, r)] = 1
        return 1

    p_memo[(n, r)] = frac(n) // frac(n - r)
    return p_memo[(n, r)]


k = int(input())
c = list(map(int, input().split()))
tiles = []

for i in range(26):
    tiles += [chr(ord("A") + i)] * c[i]

s = 0
n = len(tiles)
for i in range(1, min(n + 1, k + 1)):
    s += permutation(n, i)

print(s)
