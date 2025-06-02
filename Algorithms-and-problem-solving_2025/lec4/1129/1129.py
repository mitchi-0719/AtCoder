def solve():
    n, r = map(int, input().split())
    if n == r == 0:
        return 1

    m = [i + 1 for i in range(n)][::-1]
    for _ in range(r):
        p, c = map(int, input().split())
        tmp = m[p - 1 : p - 1 + c]
        m = tmp + m[: p - 1] + m[p - 1 + c :]

    print(m[0])


while 1:
    if solve():
        break
