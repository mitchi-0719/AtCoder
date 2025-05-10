while True:
    n, m, p = map(int, input().split())

    if n == m == p == 0:
        exit()

    x = []
    for i in range(n):
        x.append(int(input()))

    x_sum = sum(x) * 100

    return_x = int(x_sum * (100 - p))

    print(return_x // x[m - 1] // 100 if x[m - 1] != 0 else 0)
