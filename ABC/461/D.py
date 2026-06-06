h, w, k = list(map(int, input().split()))

s = [[int(si) for si in input()] for _ in range(h)]


def solve(ls, b):
    cnt = 0
    for l in range(w):
        su = 0
        r = l

        while r < w and su + ls[r] <= b:
            su += ls[r]
            r += 1

        cnt += r - l

    return cnt


cnt = 0
for u in range(h):
    ls = [0] * w
    for d in range(u, h):
        for j in range(w):
            ls[j] += s[d][j]

        cnt += solve(ls, k) - solve(ls, k - 1)

print(cnt)
