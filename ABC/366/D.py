n = int(input())
a = [[[0] * (n + 1)] * (n + 1)] + [
    [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for i in range(n)]
    for j in range(n)
]
q = int(input())
acc = [[[0] * (n + 1) for i in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            acc[i][j][k] = (
                acc[i - 1][j][k]
                + acc[i][j - 1][k]
                + acc[i][j][k - 1]
                - acc[i - 1][j - 1][k]
                - acc[i - 1][j][k - 1]
                - acc[i][j - 1][k - 1]
                + acc[i - 1][j - 1][k - 1]
                + a[i][j][k]
            )

for _ in range(q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    lx -= 1
    ly -= 1
    lz -= 1

    print(
        acc[rx][ry][rz]
        - acc[lx][ry][rz]
        - acc[rx][ly][rz]
        - acc[rx][ry][lz]
        + acc[lx][ly][rz]
        + acc[lx][ry][lz]
        + acc[rx][ly][lz]
        - acc[lx][ly][lz]
    )
