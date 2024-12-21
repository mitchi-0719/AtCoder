h, w, x, y = map(int, input().split())
s = [list(input()) for _ in range(h)]

t = input()
nx, ny = x - 1, y - 1

cnt = 0
for ti in t:
    if ti == "U":
        if nx - 1 >= 0 and s[nx - 1][ny] != "#":
            if s[nx - 1][ny] == "@":
                s[nx - 1][ny] = "."
                cnt += 1
            nx -= 1
    elif ti == "D":
        if nx + 1 < h and s[nx + 1][ny] != "#":
            if s[nx + 1][ny] == "@":
                s[nx + 1][ny] = "."
                cnt += 1
            nx += 1
    elif ti == "L":
        if ny - 1 >= 0 and s[nx][ny - 1] != "#":
            if s[nx][ny - 1] == "@":
                s[nx][ny - 1] = "."
                cnt += 1
            ny -= 1
    elif ti == "R":
        if ny + 1 < w and s[nx][ny + 1] != "#":
            if s[nx][ny + 1] == "@":
                s[nx][ny + 1] = "."
                cnt += 1
            ny += 1

print(nx + 1, ny + 1, cnt)
