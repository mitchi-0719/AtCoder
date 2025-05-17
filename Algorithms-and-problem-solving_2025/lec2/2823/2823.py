def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return True

    rec = [0 for _ in range(m)]
    for _ in range(n):
        d, v = map(int, input().split())
        d -= 1
        rec[d] = max(rec[d], v)

    print(sum(rec))


while 1:
    if solve():
        break
