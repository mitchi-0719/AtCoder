N, K = map(int, input().split())
A = list(map(int, input().split()))

c = [2] * (N + 1)
for a in A:
    c[a] = 1
s = []
for i in range(1, N + 1):
    for _ in range(c[i]):
        s.append(i)
M = len(s)

l, r = [0] * (M + 1), [0] * (M + 1)
for i in range(2, M + 1, 2):
    l[i] = l[i - 2] + (s[i - 1] - s[i - 2])
for i in range(M - 2, -1, -2):
    r[i] = r[i + 2] + (s[i + 1] - s[i])

if M % 2:
    print(min(l[i] + r[i + 1] for i in range(0, M, 2)))
else:
    print(l[M])
