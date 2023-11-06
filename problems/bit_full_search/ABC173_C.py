h, w, k = map(int, input().split())
c = []

for i in range(h):
    c.append(input())


def count_cell(b1, b2):
    exclude_x = []
    exclude_y = []
    cnt = 0

    for i in range(h):
        if b1 & (1 << i):
            exclude_y.append(i)

    for i in range(w):
        if b2 & (1 << i):
            exclude_x.append(i)

    for i in range(h):
        if i in exclude_y:
            continue
        for j in range(w):
            if j in exclude_x:
                continue
            cnt += 1 if c[i][j] == "#" else 0

    return cnt


ans = 0
for bit1 in range(1 << h):
    for bit2 in range(1 << w):
        if count_cell(bit1, bit2) == k:
            ans += 1

print(ans)
