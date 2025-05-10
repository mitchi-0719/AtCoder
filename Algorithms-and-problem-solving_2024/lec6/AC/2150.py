from bisect import bisect
import math

prime = [2]
alpha_cnt = 0
i = 3

while alpha_cnt < 101:
    judge = True
    for j in range(3, int(math.sqrt(i) + 1), 2):
        if i % j == 0:
            judge = False
            break
    if judge:
        if i >= 10**5:
            alpha_cnt += 1
        prime.append(i)
    i += 2


def solve(n, p):
    ni = bisect(prime, n)
    l = []
    for i in range(p + 1):
        for j in range(i, p + 1):
            l.append(prime[i + ni] + prime[j + ni])

    print(sorted(l)[p - 1])


while True:
    n, p = map(int, input().split())
    if n == p == -1:
        exit()
    solve(n, p)
