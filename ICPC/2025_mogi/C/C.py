import math


def solve():
    n, k = map(int, input().split())
    if n == k == 0:
        return 1

    div = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            div.append(i)
            div.append(n // i)
    div = sorted(set(div))

    ans = 0
    for d in div:
        ans += k * (n // d)


    ans %= n
    print("Yes" if ans == 0 else "No")


while 1:
    if solve():
        break
