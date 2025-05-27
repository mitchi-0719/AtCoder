from collections import defaultdict


def solve():
    n = int(input())
    if n == 0:
        return 1

    d = defaultdict(int)
    dg = defaultdict(int)

    for _ in range(n):
        y, _, m = input().split()
        y = int(y)

        d[y] += 1
        if m == "Gold":
            dg[y] += 1

    print(
        max(sorted(dg.items(), key=lambda x: x[0]), key=lambda x: x[1])[0],
        max(sorted(d.items(), key=lambda x: x[0]), key=lambda x: x[1])[0],
    )


while 1:
    if solve():
        break
