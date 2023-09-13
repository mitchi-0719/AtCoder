#正解

n = int(input())
A = list(map(int, input().split()))

A = sorted(A)
buffer = A[0]
cnt = 0

for i in range(n):
    if buffer != A[i]:
        buffer = A[i]
        cnt += 1
cnt += 1
print(cnt)