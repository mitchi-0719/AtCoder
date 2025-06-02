def solve():
    n, m, p = map(int, input().split())
    if n == m == p == 0:
        return 1

    x = [int(input()) for _ in range(n)]
    if x[m - 1] == 0:
        print(0)
    else:
        print(int(sum(x) / x[m - 1] * (100 - p)))


while 1:
    if solve():
        break
