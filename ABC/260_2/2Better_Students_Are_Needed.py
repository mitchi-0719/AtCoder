#clear

n, x, y, z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

check = [True]*n
id = []

i = 0
while(i < x):
    idx = 0
    max = -1
    for j in range(n):
        if check[j]:
            if max < A[j]:
                idx = j
                max = A[idx]
    id.append(idx + 1)
    check[idx] = False
    i += 1

i = 0
while(i < y):
    idx = 0
    max = -1
    for j in range(n):
        if check[j]:
            if max < B[j]:
                idx = j
                max = B[idx]
    id.append(idx + 1)
    check[idx] = False
    i += 1

if z != 0:
    C = [0]*n
    for j in range(n):
        C[j] = A[j] + B[j]

    i = 0
    while(i < z):
        idx = 0
        max = -1
        for j in range(n):
            if check[j]:
                if max < C[j]:
                    idx = j
                    max = C[idx]
        id.append(idx + 1)
        check[idx] = False
        i += 1

id.sort()
for j in range(x + y + z):
    print(id[j])
