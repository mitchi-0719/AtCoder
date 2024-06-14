n = int(input())
li = [[0 for _ in range(n)] for __ in range(n)]
li[n // 2][n // 2] = "T"
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
d_idx = 0

i = 0
j = 0

for k in range(n**2):
    if li[i][j] == "T":
        break

    li[i][j] = k + 1
    next_i = i + dire[d_idx][1]
    next_j = j + dire[d_idx][0]
    if next_i < n and next_j < n and li[next_i][next_j] == 0:
        i = next_i
        j = next_j
    else:
        d_idx = (d_idx + 1) % 4
        i += dire[d_idx][1]
        j += dire[d_idx][0]

for l in li:
    print(*l)
