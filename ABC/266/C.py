def cross(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


def solve(vertexes):
    for i in range(4):
        a = vertexes[i % 4]
        b = vertexes[(i + 1) % 4]
        c = vertexes[(i + 2) % 4]

        vec_ab = [b[0] - a[0], b[1] - a[1]]
        vec_bc = [c[0] - b[0], c[1] - b[1]]

        if cross(*vec_ab, *vec_bc) < 0:
            return False

    return True


square = []

for _ in range(4):
    square.append(list(map(int, input().split())))

print("Yes" if solve(square) else "No")
