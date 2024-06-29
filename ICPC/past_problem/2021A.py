while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0]:
        exit()

    while a.count(0) != 3:
        m = min([i for i in a if i > 0])
        mi = a.index(m)

        for i in range(4):
            if i != mi:
                if a[i] - m <= 0:
                    a[i] = 0
                else:
                    a[i] -= m

    print(max(a))
