def judge(i, j):
    move = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
    st = ["" for _ in range(8)]
    c = "snuke"

    for k in range(5):
        for l, m in enumerate(move):
            x, y = m
            if 0 <= i + k * y < h and 0 <= j + k * x < w:
                st[l] += s[i + k * y][j + k * x]

    for k in range(8):
        if st[k] == c:
            x, y = move[k]
            for l in range(5):
                print(i + l * y + 1, j + l * x + 1)
            exit()


h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            judge(i, j)
