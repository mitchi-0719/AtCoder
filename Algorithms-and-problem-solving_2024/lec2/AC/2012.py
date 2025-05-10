# AC

import itertools


def solve(e):
    ans = float("inf")
    for z in itertools.count():
        if z**3 > e:
            break
        for y in itertools.count():
            if z**3 + y**2 > e:
                break
            x = e - (z**3 + y**2)
            ans = min(ans, x + y + z)
    print(ans)


while True:
    e = int(input())
    if e == 0:
        exit()

    solve(e)
