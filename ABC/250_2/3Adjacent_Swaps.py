#不正解

n, q = map(int, input().split())
X = [int(input()) for i in range(q)]
A = [i for i in range(1, n + 1)]

for i in range(q):
    idx = A.index(X[i])
    if idx == len(A) - 1:
        buffer = A[idx]
        A[idx] = A[idx - 1]
        A[idx - 1] = buffer
    else:
        if i < q - 1 and A[idx + 1] == X[i + 1]: continue
        else:
            buffer = A[idx]
            A[idx] = A[idx + 1]
            A[idx + 1] = buffer

for i in A:
    print(i, end=" ")