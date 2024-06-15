def solve(n):
    sx, sy, gx, gy = map(int, input().split())
    sensor = [list(map(int, input().split())) for _ in range(n)]
    w = h = 1000

    dp = [[float("inf") for _ in range(w)]]


while True:
    n = int(input())
    if n == 0:
        exit()

    solve(n)
