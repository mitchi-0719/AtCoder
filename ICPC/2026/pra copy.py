s = 4
k = int(input())


def check(s, k, m):
    start = ((m - 1) * ((4 * s - 2) + (m + 1) - 2)) / 2
    count = s * 2 - 2 * m + 1
    print(m, start, count)
    return k <= start + count


l = 1
r = s + 1
m = (l + r) // 2
while r >= l:
    if not check(s, k, m):
        l = m + 1
    else:
        r = m - 1
    print(l, r, m)

print(l)
