#正解

n = int(input())

A = [[0 for i in range(n)] for j in range(n)]

A[0][0] = 1
for i in range(1, n):
    A[i][0] = 1
    for j in range(1, i + 1):
        A[i][j] = A[i - 1][j] + A[i - 1][j - 1]

for i in range(n):
    printer = ""
    k = 0
    while k < n and A[i][k] != 0:
        printer += str(A[i][k]) + " "
        k += 1
    print(printer)