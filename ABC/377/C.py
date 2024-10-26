n, m = map(int, input().split())
piece = [list(map(int, input().split())) for _ in range(m)]

ans = n**2
ng = set()
move = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
for p in piece:
    px, py = p
    ng.add((px, py))
    for mv in move:
        x, y = mv
        if 0 < px + x <= n and 0 < py + y <= n:
            ng.add((px + x, py + y))

print(ans - len(ng))
