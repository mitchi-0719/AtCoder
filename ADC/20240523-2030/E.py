import itertools
import bisect

n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)

acc = list(itertools.accumulate(sorted_a[::-1]))

for i in range(n):
    idx = bisect.bisect_right(sorted_a, a[i])
    if idx == n:
        print(0, end=" ")
    else:
        print(acc[-(idx + 1)], end=" ")
