from itertools import accumulate

n, m = map(int, input().split())
a = list(map(int, input().split()))
acc = list(accumulate(a[:-1]))

print(acc)
