def solve(n, m):
    max_up = n**n
    max_down = m**m


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        exit()

    solve(n, m)
