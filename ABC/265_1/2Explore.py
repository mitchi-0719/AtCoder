#不正解

n, m, t = map(int, input().split())
A = list(map(int, input().split()))
X = [0] * m
Y = [0] * m

for i in range(n):
    X[i], Y[i] = map(int, input().split())

x_idx = 0
i = 0

while i < n - 2 and t > 0:
    t -= A[i]
    if x_idx < m and  X[x_idx] == i + 1:
        t += Y[x_idx]
        x_idx += 1
    i += 1

if i == n:
    print("Yes")
else:
    print("No")