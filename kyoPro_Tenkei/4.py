#AC

h, w = map(int, input().split())
A = [list(map(int, input().split())) for i in range(h)]

col_sum = [0] * w
row_sum = [0] * h

for i in range(w):
    for j in range(h):
        col_sum[i] += A[j][i]
        row_sum[j] += A[j][i]

for i in range(h):
    for j in range(w):
        ans = col_sum[j] + row_sum[i] - A[i][j]
        print(ans, end=" ")
    print()