import itertools
from collections import defaultdict


def solve(n, m):
    h = [int(input()) for _ in range(n)]
    w = [int(input()) for _ in range(m)]

    h_acc = [0] + list(itertools.accumulate(h))
    w_acc = [0] + list(itertools.accumulate(w))

    d1 = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n + 1):
            d1[h_acc[j] - h_acc[i]] += 1

    d2 = defaultdict(int)
    for i in range(m):
        for j in range(i + 1, m + 1):
            d2[w_acc[j] - w_acc[i]] += 1

    ans = 0
    for k, v in d1.items():
        ans += d2[k] * v

    print(ans)


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        exit()
    solve(n, m)
