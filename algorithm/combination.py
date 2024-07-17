from collections import defaultdict


def factorial(n, memo=defaultdict(int)):
    if memo[n] == 0:
        if n == 1:
            memo[n] = 1
        else:
            memo[n] = n * factorial(n - 1, memo)

    return memo[n]


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
