def to_tuple(l):
    sort_l = sorted(l, key=lambda x: (x[0], x[1]))
    return tuple(tuple(li) for li in sort_l)


def check(i, j):
    li = [
        [[0, -1], [-1, -1]],
        [[0, -1], [1, -1]],
        [[-1, 0], [-1, -1]],
        [[-1, 0], [-1, 1]],
        [[0, 1], [-1, 1]],
        [[0, 1], [1, 1]],
        [[1, 0], [1, -1]],
        [[1, 0], [1, 1]],
        [[0, -1], [-1, 0]],
        [[-1, 0], [0, 1]],
        [[0, 1], [1, 0]],
        [[1, 0], [0, -1]],
    ]

    for c1, c2 in li:
        x1, y1 = c1
        x2, y2 = c2

        if (
            0 <= j + x1 < n
            and 0 <= i + y1 < n
            and 0 <= j + x2 < n
            and 0 <= i + y2 < n
            and s[i + y1][j + x1] == s[i + y2][j + x2] == "o"
        ):
            print(i, j, x1, y1, x2, y2)
            ans.add(to_tuple([[i, j], [i + y1, j + x1], [i + y2, j + x2]]))


n = int(input())
s = [list(input()) for _ in range(n)]
ans = set()

for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            check(i, j)

print(len(ans))
