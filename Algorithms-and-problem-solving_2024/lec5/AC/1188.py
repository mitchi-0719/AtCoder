from collections import deque, defaultdict
import math
import sys

sys.setrecursionlimit(10**8)


def solve(s, f, l, d):
    if s[f] != "[":
        n = int(s[f : l + 1])
        return math.ceil(n / 2)
    else:
        arr = []
        i = f
        while i <= l:
            if s[i] == "[":
                g = solve(s, i + 1, d[i] - 1, d)
                arr.append(g)
                i = d[i] + 1
            else:
                i += 1
        ans = sum(sorted(arr)[: math.ceil(len(arr) / 2)])
        return ans


def idx(s):
    stack = deque()
    d = defaultdict(int)
    for i, si in enumerate(s):
        if si == "[":
            stack.append(i)
        elif si == "]":
            d[stack.pop()] = i

    return d


n = int(input())

for _ in range(n):
    s = input()
    d = idx(s)
    print(solve(s, 1, len(s) - 1, d))
