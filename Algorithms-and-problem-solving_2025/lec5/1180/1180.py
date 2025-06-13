from collections import defaultdict


def solve():
    a0, l = map(int, input().split())
    if a0 == l == 0:
        return 1

    s = list(str(a0)) + (l - len(str(a0))) * ["0"]
    mx = int("".join(sorted(s, reverse=True)))
    mn = int("".join(sorted(s)))
    d = defaultdict(lambda: -1)

    i = 1
    d[a0] = 0
    while True:
        ai = mx - mn
        if d[ai] != -1:
            print(d[ai], ai, i - d[ai])
            break

        d[ai] = i
        i += 1

        s = list(str(ai)) + (l - len(str(ai))) * ["0"]
        mx = int("".join(sorted(s, reverse=True)))
        mn = int("".join(sorted(s)))


while not solve():
    ...
