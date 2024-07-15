from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


def dfs(n, a, b, x, now, memo=defaultdict(int)):
    if memo[now] != 0:
        return memo[now] == 1

    if now == x:
        memo[now] = 1

    elif now in b or now > x:
        memo[now] = -1

    else:
        judge = False
        for i in range(n):
            new_now = now + a[i]
            if new_now in b or new_now > x:
                continue
            judge = judge or dfs(n, a, b, x, new_now, memo)
            if judge:
                break
        memo[now] = 1 if judge else -1

    return memo[now] == 1


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
x = int(input())

print("Yes" if dfs(n, a, b, x, 0) else "No")
