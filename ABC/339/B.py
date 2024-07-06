h, w, n = map(int, input().split())
g = [[False for _ in range(w)] for __ in range(h)]

x = 0
y = 0
dire = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_i = 0

for i in range(n):
    g[y % h][x % w] = not g[y % h][x % w]

    if not g[y % h][x % w]:
        dir_i -= 1
        x += dire[dir_i % 4][0]
        y += dire[dir_i % 4][1]
    else:
        dir_i += 1
        x += dire[dir_i % 4][0]
        y += dire[dir_i % 4][1]

for i in range(h):
    for j in range(w):
        print("#" if g[i][j] else ".", end="")
    print()
