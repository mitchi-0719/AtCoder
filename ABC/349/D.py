import math

l, r = map(int, input().split())
lr = []

if l == 0:
    s = int(math.log2(r))
    lr.append((0, 2**s))

print(len(lr))
for i in lr:
    print(*i)
