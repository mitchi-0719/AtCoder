#正解

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

for i in range(w):
    for j in range(h):
        print(A[j][i], end=" ")
    print()