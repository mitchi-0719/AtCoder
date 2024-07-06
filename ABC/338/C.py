n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(10**6 + 1):
    fin = False
    for j in range(n):
        if a[j] * i > q[j]:
            fin = True
            break

    if fin:
        break

    tmp = float("inf")
    for j in range(n):
        if b[j] == 0:
            continue
        tmp = min(tmp, (q[j] - a[j] * i) // b[j])

    if tmp >= 0:
        ans = max(ans, i + tmp)

print(ans)
