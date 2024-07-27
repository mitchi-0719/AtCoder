def move(c, xi, x, y, w, h):
    if xi == "L":
        if x != 0 and c[y][x - 1] != "#":
            return x - 1, y
    elif xi == "R":
        if x != w - 1 and c[y][x + 1] != "#":
            return x + 1, y
    elif xi == "U":
        if y != 0 and c[y - 1][x] != "#":
            return x, y - 1
    else:
        if y != h - 1 and c[y + 1][x] != "#":
            return x, y + 1
    return x, y


h, w = map(int, input().split())
y, x = map(int, input().split())
c = [list(input()) for _ in range(h)]

X = list(input())
y -= 1
x -= 1
for xi in X:
    x, y = move(c, xi, x, y, w, h)


print(y + 1, x + 1)
