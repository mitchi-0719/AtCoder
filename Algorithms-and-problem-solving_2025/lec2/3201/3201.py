def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return True

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = [0] * 10
    for ai in a:
        for bi in b:
            s = str(ai * bi)
            for si in s:
                ans[int(si)] += 1

    print(*ans)


while 1:
    if solve():
        break
