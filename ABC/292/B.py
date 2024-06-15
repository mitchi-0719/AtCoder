n, q = map(int, input().split())
c = [0 for _ in range(n)]

for _ in range(q):
    s, i = map(int, input().split())
    if s == 1:
        c[i - 1] += 1
    elif s == 2:
        c[i - 1] += 2
    else:
        print("Yes" if c[i - 1] >= 2 else "No")
