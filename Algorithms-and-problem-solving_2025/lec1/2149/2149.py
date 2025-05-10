def f(a, b, c, x):
    return (a * x + b) % c


def solve():
    n, a, b, c, x = map(int, input().split())

    if (n, a, b, c, x) == (0, 0, 0, 0, 0):
        return False

    y = list(map(int, input().split()))
    ans = 0

    r = x
    for i in range(n):
        if y[i] >= c:
            print(-1)
            return True

        while r != y[i]:
            r = f(a, b, c, r)
            ans += 1

            if ans > 10000:
                print(-1)
                return True

        if i + 1 < n and y[i + 1] == r:
            ans += 1
            r = f(a, b, c, r)

        if ans > 10000:
            print(-1)
            return True

    print(ans)
    return True


while 1:
    if not solve():
        break
