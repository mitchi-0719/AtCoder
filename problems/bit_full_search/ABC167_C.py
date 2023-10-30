from itertools import product

n, m, x = map(int, input().split())
a = []
c = []

for i in range(n):
    li = list(map(int, input().split()))
    c.append(li[0])
    a.append(li[1:])


def judge(bit):
    amount = 0
    lev = [0 for _ in range(m)]
    for i, b in enumerate(bit):
        if b == 1:
            amount += c[i]
            for j in range(m):
                lev[j] += a[i][j]
    return min(lev) >= x, amount


ans = -1
for bit in product((0, 1), repeat=n):
    res, amount = judge(bit)
    if res and (ans == -1 or amount < ans):
        ans = amount

print(ans)
