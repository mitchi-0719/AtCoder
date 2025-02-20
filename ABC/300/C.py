def check(i, j, d):
    return (
        c[i + d][j + d] == "#"
        and c[i + d][j - d] == "#"
        and c[i - d][j + d] == "#"
        and c[i - d][j - d] == "#"
    )


def rep(i, j, d):
    c[i + d][j + d] = "."
    c[i + d][j - d] = "."
    c[i - d][j + d] = "."
    c[i - d][j - d] = "."


def solve(i, j):
    if c[i][j] != "#":
        return 0

    d = 1
    while 0 <= i - d < h and 0 <= j - d < w and 0 <= i + d < h and 0 <= j + d < w:
        if not check(i, j, d):
            return d - 1
        rep(i, j, d)
        d += 1

    return d - 1


h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = [0 for _ in range(min(h, w))]

for i in range(h):
    for j in range(w):
        s = solve(i, j) - 1
        if s != -1:
            ans[s] += 1

print(*ans)
