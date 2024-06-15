n, m = map(int, input().split())
l = 1
r = n
for i in range(m):
    li, ri = map(int, input().split())
    if l < li:
        l = li
    if ri < r:
        r = ri

print(max(0, r - l + 1))
