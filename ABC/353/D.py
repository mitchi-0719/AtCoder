# TLE

n = int(input())
a = list(map(int, input().split()))

m = 998244353
s = 0

for i in range(0, n - 1):
    for j in range(i + 1, n):
        s += int(str(a[i]) + str(a[j]))

print(s % m)
