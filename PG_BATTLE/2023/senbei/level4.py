from copy import copy

n, k = map(int, input().split())
a = list(map(int, input().split()))

sets = set([])

def rep(a, i):
    if i+k < n:
        a[i], a[i+k] = a[i+k], a[i]
        sets.add(tuple(a))
        rep(a, i+1)

for i in range(n-k):
    sets.add(tuple(a))
    rep(copy(a), i)

print(len(sets))