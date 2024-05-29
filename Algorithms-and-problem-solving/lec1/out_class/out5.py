def solve(n, m, p, q, x):
    if judge(p, q, x):
        print("OK")
        return

    i = 0
    now = p
    while i <= m:
        if now == 1:
            temp = [*x]
            temp.insert(i, 1)
            if judge(p, q, temp):
                print(1, i)
                return
        elif now == n:
            temp = [*x]
            temp.insert(i, n - 1)
            if judge(p, q, temp):
                print(n - 1, i)
                return
        else:
            temp = [*x]
            temp.insert(i, now)
            if judge(p, q, temp):
                print(now, i)
                return
            temp = [*x]
            temp.insert(i, now - 1)
            if judge(p, q, temp):
                print(now - 1, i)
                return

        if i == m:
            break
        if now == x[i]:
            now += 1
        elif now == x[i] + 1:
            now -= 1
        i += 1

    print("NG")


def judge(p, q, x):
    now = p
    for r in x:
        if now == r:
            now += 1
        elif now == r + 1:
            now -= 1

    return now == q


while True:
    n, m, p, q = map(int, input().split())
    if n == m == p == q == 0:
        exit()

    x = list(map(int, input().split()))

    solve(n, m, p, q, x)
