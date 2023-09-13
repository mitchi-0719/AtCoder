#不正解

n, k = map(int, input().split())

A = list(map(int, input().split()))

sortA = sorted(A)

for i in range(n - k):
    if A[i] > A[i + k]:
        buffer = A[i]
        A[i] = A[i + k]
        A[i + k] = buffer

if A == sortA:
    print("Yes")
else:
    print("No")