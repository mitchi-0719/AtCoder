from collections import defaultdict

memo = defaultdict(int)


def factorial(n):
    if memo[n] == 0:
        if n == 1:
            memo[n] = 1
        else:
            memo[n] = n * factorial(n - 1)

    return memo[n]


s = input()
ans = factorial(len(s)) - len(s)

print(ans)
