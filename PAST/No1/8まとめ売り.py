#不正解

import copy

n = int(input())
C = list(map(int, input().split()))
q = int(input())
S = [list(map(int, input().split())) for _ in range(q)]

total = 0

for i in range(q):
    query = S[i]
    if query[0] == 1:
        if C[query[1]-1] >= query[2]:
            C[query[1]-1] -= query[2]
            total += query[2]
    elif query[0] == 2:
        idx = 0
        C_copy = copy.copy(C)
        buffer = 0
        while idx < n and C[idx] >= query[1]:
            C_copy[idx] -= query[1]
            buffer += query[1]
            idx += 2
        if idx >= n:
            C = C_copy
            total += buffer
    else:
        idx = 0
        C_copy = copy.copy(C)
        buffer = 0
        while idx < n and C[idx] >= query[1]:
            C_copy[idx] -= query[1]
            buffer += query[1]
            idx += 1
        if idx >= n:
            C = C_copy
            total += buffer
print(total)