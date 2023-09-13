# AC

import itertools

n, k = map(int, input().split())

a = []
b = []

cumulative_sum = []

for i in range(n):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

a, b = zip(*sorted(zip(a, b), reverse=True))
a = list(a)
b = list(b)

for i in itertools.accumulate(b):
    cumulative_sum.append(i)

idx = n-1

if cumulative_sum[idx] <= k:
    print(1)
    exit()

while idx >= 0:
    idx -= 1
    if cumulative_sum[idx] <= k:
        print(a[idx+1]+1)
        exit()

print(a[0]+1)