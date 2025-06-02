def solve():
    h, w = map(int, input().split())
    if h == w == 0:
        return 1

    v = [list(map(int, list(input()))) for _ in range(h)]
    print(v)


while 1:
    if solve():
        break
