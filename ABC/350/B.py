n, q = map(int, input().split())
t = list(map(int, input().split()))

_t = [True for _ in range(n)]

for ti in t:
    _t[ti - 1] = not _t[ti - 1]

print(len([0 for ti in _t if ti]))
