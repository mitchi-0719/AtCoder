import bisect
import itertools

n, q = map(int, input().split())
r = list(itertools.accumulate(sorted(list(map(int, input().split())))))

for i in range(q):
    x = int(input())
    print(bisect.bisect(r, x))
