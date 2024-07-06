from collections import deque
from copy import deepcopy


def to_tuple(arr):
    return tuple(tuple(a) for a in arr)


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

d = {to_tuple(A): 0}
q = deque([A])
while len(q) > 0:
    a = q.popleft()
    for i in range(H - 1):
        b = deepcopy(a)
        b[i], b[i + 1] = b[i + 1], b[i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            q.append(b)

    for i in range(W - 1):
        b = deepcopy(a)
        for j in range(H):
            b[j][i], b[j][i + 1] = b[j][i + 1], b[j][i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            q.append(b)

print(d[to_tuple(B)] if to_tuple(B) in d else -1)
