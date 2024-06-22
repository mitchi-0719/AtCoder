import sys

sys.setrecursionlimit(10**8)


def solve(n, s, i):
    l = len(s[i])
    if s[i][-1] in "+*":
        ans = 0
        if s[i][-1] == "*":
            ans = 1
        for j in range(i + 1, n):
            if len(s[j]) == l + 1:
                if s[i][-1] == "+":
                    ans += solve(n, s, j)
                else:
                    ans *= solve(n, s, j)
            elif len(s[j]) <= l:
                break
        return ans
    else:
        return int(s[i][-1])


while True:
    n = int(input())
    if n == 0:
        exit()
    s = [input() for _ in range(n)]
    print(solve(n, s, 0))
