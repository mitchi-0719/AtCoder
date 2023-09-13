n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0

s = [0 for _ in range(n)]

s[0] = a[0]
for i in range(1, n):
    s[i] = s[i-1] + a[i]

print(s)