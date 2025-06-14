from collections import defaultdict


def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return 1

    dic = defaultdict(int)
    for _ in range(n):
        d, v = map(int, input().split())
        dic[d] = max(dic[d], v)

    print(sum(dic.values()))


while not solve():
    ...
