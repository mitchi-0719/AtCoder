# AC

n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

i1 = p-1
i2 = r-1
for i in range(q-p+1):

    a[i1], a[i2] = a[i2], a[i1]
    i1 += 1
    i2 += 1

for i in range(n):
    print(a[i], end=" ")