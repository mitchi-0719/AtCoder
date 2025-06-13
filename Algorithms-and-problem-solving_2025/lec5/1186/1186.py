def solve():
    h, w = map(int, input().split())
    if h == w == 0:
        return 1

    hw = h**2 + w**2

    for ai in arr:
        if ai[0] > hw or (ai[0] == hw and ai[1] > h):
            print(*ai[1:])
            return


arr = []
for h in range(1, 151):
    for w in range(h + 1, 151):
        arr.append((h**2 + w**2, h, w))

arr = sorted(arr)
while not solve():
    ...
