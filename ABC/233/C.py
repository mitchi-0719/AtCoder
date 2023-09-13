n, x = map(int, input().split())
a = []

for i in range(n):
    A = list(map(int, input().split()))
    a.append(A[1:])

pro = 1
i = 0
idxs = [0 for j in range(n)]
while i < n:
    pro *= a[i][idxs[i]]