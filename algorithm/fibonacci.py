from collections import defaultdict


def fibonacci(n, memo=defaultdict(lambda: float("inf"))):
    if memo[n] != float("inf"):
        return memo[n]

    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
print(fibonacci(n))
