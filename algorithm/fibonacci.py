from collections import defaultdict

memo = defaultdict(int)


def fibonacci(n):
    if memo[n] != 0:
        return memo[n]

    if n == 1 or n == 2:
        memo[n] = 1
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


for i in range(1, 10):
    print(fibonacci(i))
