#answer

x, a, d, n = map(int, input().split())

if d < 0:
    a = a + d * (n - 1)
    d *= -1

top = n - 1
bottom = 0


while top >= bottom:
    mid = (top + bottom) // 2
    if a + d * mid < x:
        bottom = mid + 1
    else:
        top = mid - 1

li = []
for i in range(-1, 1):
    li.append(abs(x - (a + d * (mid + i))))

print(min(li))