n, q = map(int, input().split())
A = list(map(int, input().split()))
X = []
K = []
for _ in range(q):
    x, k = map(int, input().split())
    X.append(x)
    K.append(k)

A_idx = [0] * n
for i in range(n):
    A_idx[i] = i

zip_list = zip(A, A_idx)
zip_list = sorted(zip_list)

A, A_idx = zip(*zip_list)
A = list(A)
A_idx = list(A_idx)
A_set = set(A)

for i in range(q):
    if X[i] not in A_set:
        print(-1)
    else:
        idx = A.index(X[i])
        cnt = 1
        while A[idx] == X[i] and cnt != K[i]:
            cnt += 1
            idx += 1
        if A[idx] == X[i]:
            print(A_idx[idx] + 1)
        else:
            print(-1)