def calc(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

l = calc(a[0], b[0], a[1], b[1])
m = calc(c[0], b[0], c[1], b[1])
n = calc(a[0], c[0], a[1], c[1])

s = l + m + n
ma = max(l, m, n)
print("Yes" if s - ma == ma else "No")
