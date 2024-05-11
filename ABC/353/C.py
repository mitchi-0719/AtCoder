# TLE

n = int(input())
a = list(map(int, input().split()))

s = 0
m = 10**8

for i in range(0, n):
    s += a[i] * (n - 1)

print(s % m)
