import math
import bisect

memo = {}
primes = []


def is_prime(n):
    if memo.get(n):
        return memo.get(n)

    if n == 1:
        memo[n] = False
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            memo[n] = False
            return memo[n]

    memo[n] = True
    return memo[n]


def solve():
    n, p = map(int, input().split())
    if n == p == -1:
        return True

    ps = []
    i = bisect.bisect_left(primes, n + 1)
    for j in range(p * 2):
        if j >= l:
            break
        for k in range(j, p * 2):
            if k >= l:
                break
            ps.append(primes[i + j] + primes[i + k])

    ps = sorted(ps)
    print(ps[p - 1])


for i in range(2, 1000000):
    if is_prime(i):
        primes.append(i)

l = len(primes)

while 1:
    if solve():
        break
