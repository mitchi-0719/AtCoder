n = int(input())
x, y, z, diff = [], [], [], []
aoki = 0
takahashi = 0

for _ in range(n):
    xi, yi, zi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    z.append(zi)
    diff.append(xi - yi)

    if xi > yi:
        takahashi += zi
    else:
        aoki += zi

print(takahashi, aoki)
print(diff)
