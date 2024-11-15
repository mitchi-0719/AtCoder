n, m = map(int, input().split())

l = list(map(int, input().split()))
l = [li + 1 for li in l]
ng = max(l)
ok = sum(l)
ans = 0
w = 0

while ng < ok:
    mid = (ok + ng) // 2
    if mid == w:
        break

    s = 0
    ans = 0
    for li in l:
        if s + li <= mid:
            s += li
        else:
            ans += 1
            s = li

    w = mid
    if ans >= m:
        ng = mid
    else:
        ok = mid

print(ok - 1)
