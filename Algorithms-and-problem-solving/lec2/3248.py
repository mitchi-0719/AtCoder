while True:
    h, w = map(int, input().split())
    if h == w == 0:
        exit()

    a = [input() for _ in range(h)]
