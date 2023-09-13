r, c = map(int, input().split())
b = []

def calc_dist(x1, y1, x2, y2):
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    return abs(x1 - x2) + abs(y1 - y2)

def bomb(x, y, p):
    for k in range(r):
        for l in range(c):
            if calc_dist(x, y, k, l) <= int(p) and not b[k][l].isdigit():
                b[k][l] = "."

for i in range(r):
    b.append(list(input()))

for i in range(r):
    for j in range(c):
        if b[i][j].isdigit():
            bomb(i, j, b[i][j])
            b[i][j] = "."

for i in range(r):
    print(*b[i], sep="")