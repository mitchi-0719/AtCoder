while True:
    max_wh = 150

    h, w = map(int, input().split())
    if h == w == 0:
        exit()

    d = h**2 + w**2
    ans = [0, 0]

    for i in range(1, max_wh + 1):
        for j in range(1, i):
            dia = i**2 + j**2
            if dia > d or (dia == d and j > h):
                ans_d = ans[0] ** 2 + ans[1] ** 2
                if ans_d == 0:
                    ans = [j, i]
                elif ans_d > dia or (dia == ans_d and i > ans[1]):
                    ans = [j, i]
    print(*ans)
