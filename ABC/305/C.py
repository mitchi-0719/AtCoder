h, w = map(int, input().split())

s = []

for i in range(h):
    s.append(input())

def search_around(x, y):
    cnt = 0
    if s[y][x] == ".":
        if x-1 >= 0 and s[y][x-1] == "#": cnt += 1
        if x+1 < w and s[y][x+1] == "#": cnt += 1
        if y-1 >= 0 and s[y-1][x] == "#": cnt += 1
        if y+1 < h and s[y+1][x] == "#": cnt += 1

    return cnt >= 2

for i in range(h):
    for j in range(w):
        if search_around(j, i):
            print(i+1, j+1)
            exit()