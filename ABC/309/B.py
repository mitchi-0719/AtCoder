# AC

n = int(input())

a = []
b = []

for i in range(n):
    A = list(input())
    B = ["0" for _ in range(n)]
    a.append(A)
    b.append(B)

for i in range(n):
    for j in range(n):
        if i == j == 0:
            b[i][j] = a[i+1][j]
        elif i == 0:
            b[i][j] = a[i][j-1]
        elif j == n-1:
            b[i][j] = a[i-1][j]
        elif i == n-1:
            b[i][j] = a[i][j+1]
        elif j == 0:
            b[i][j] = a[i+1][j]
        else:
            b[i][j] = a[i][j]

for i in range(n):
    for j in range(n):
        print(b[i][j], end="")
    print()