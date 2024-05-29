# AC

while True:
    r0, w0, c, r = map(int, input().split())
    if r0 == w0 == c == r == 0:
        exit()

    i = 0
    while True:
        if r0 + i * r >= c * w0:
            break
        i += 1

    print(i)
