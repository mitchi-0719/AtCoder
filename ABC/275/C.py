import math

s = []
dists = {}

for i in range(9):
    S = input()
    s.append(S)

def search(x, y):
    for i in range(9):
        for j in range(9):
            if [i, j] != [x, y] and s[i][j] == "#":
                

def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

for i in range(9):
    for j in range(9):
        if s[i][j] == "#":
            search(i, j)

cnt = 0
for i, k in dists.items():
    keys = []
    sub_cnt = 1
    for j, l in dists.items():
        if sub_cnt == 4:
            break
        elif k == l:
            sub_cnt += 1
            if i in keys:
                keys.append(j)
            else:
                keys.append(i)
    if sub_cnt == 4:
        for m in keys:
            print(m)
            del dists[m]
        cnt += 1

print(cnt)