n = int(input())
w = "."
b = "#"

s = [[b for _ in range(3**n)] for __ in range(3**n)]


def solve(level, sx, sy, isCenter):
    if level == 0:
        if isCenter:
            s[sy][sx] = w
        return

    if isCenter:
        for i in range(3**level):
            for j in range(3**level):
                s[sy + i][sx + j] = w
        return

    for i in range(9):
        _sx = sx + (i % 3) * 3 ** (level - 1)
        _sy = sy + (i // 3) * 3 ** (level - 1)
        solve(level - 1, _sx, _sy, i == 4)


solve(n, 0, 0, False)


for _s in s:
    for si in _s:
        print(si, end="")
    print()
