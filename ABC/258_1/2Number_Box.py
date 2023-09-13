#不正解
n = int(input())

A = [list(input()) for l in range(n)]

max_value = max(A[0])
for i in range(1, n):
    buffer = max(A[i])
    if max_value < buffer:
        max_value = buffer
