tanku = [5, 7, 5, 7, 7]


def solve():
    n = int(input())
    if n == 0:
        return 1

    w = [input() for _ in range(n)]

    for i in range(n):
        j = 0
        c = [*tanku]
        for wi in w[i:]:
            if c[j] - len(wi) < 0:
                break
            c[j] -= len(wi)
            if c[j] == 0:
                j += 1

            if j == 5:
                print(i + 1)
                return

        else:
            print(i + 1)
            return


while not solve():
    ...
