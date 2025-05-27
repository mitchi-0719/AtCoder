import math

memo = {}


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
    a, d, n = map(int, input().split())
    if a == d == n == 0:
        return True

    an = a
    cnt = 0
    while True:
        if is_prime(an):
            cnt += 1
            if cnt == n:
                print(an)
                break

        an += d


while 1:
    if solve():
        break
