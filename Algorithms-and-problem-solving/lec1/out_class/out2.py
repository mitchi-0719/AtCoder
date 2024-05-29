def flat(arr):
    ar = []
    for a in arr:
        ar += a

    return ar


def solve(h, w, r, s):
    now = 0
    flat_r = flat(r)
    ans = 0

    for c in s:
        i = flat_r.index(c)
        nr = now // w
        ir = i // w
        nc = now % w
        ic = i % w

        ans += abs(nc - ic) + abs(nr - ir) + 1

        now = i

    print(ans)


while True:
    h, w = map(int, input().split())
    if h == w == 0:
        exit()

    r = [input() for _ in range(h)]
    s = input()

    solve(h, w, r, s)
