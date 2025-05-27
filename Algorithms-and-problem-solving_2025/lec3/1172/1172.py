import math
import bisect

memo = {}
primes = []


def is_prime(n):
    if memo.get(n):
        return memo.get(n)

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            memo[n] = False
            return memo[n]

    memo[n] = True
    return memo[n]


def solve():
    n = int(input())
    if n == 0:
        return True

    i1 = bisect.bisect(primes, n)
    i2 = bisect.bisect(primes, n * 2)

    print(i2 - i1)


for i in range(2, 123456 * 2 + 1):
    if is_prime(i):
        primes.append(i)

while 1:
    if solve():
        break
