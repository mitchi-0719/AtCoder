def solve():
    n = int(input())
    if n == 0:
        return True

    s = [int(input()) for _ in range(n)]
    su = sum(s)
    mx = max(s)
    mn = min(s)

    print((su - mx - mn) // (n - 2))


while 1:
    if solve():
        break
