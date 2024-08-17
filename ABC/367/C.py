import sys

sys.setrecursionlimit(10**9)


def solve(li, r, i, n, k):
    if i == n:
        if sum(li) % k == 0:
            print(*li)
        return

    for j in range(1, r[i] + 1):
        solve([*li], r, i + 1, n, k)
        li[i] += 1


n, k = map(int, input().split())
r = list(map(int, input().split()))
solve([1] * n, r, 0, n, k)
