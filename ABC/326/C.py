from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
max_count = 0

for i in range(n):
    max_count = max(max_count, bisect_left(a, a[i] + m) - i)

print(max_count)