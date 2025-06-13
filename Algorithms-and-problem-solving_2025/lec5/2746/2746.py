def encode(b):
    s = ""
    n = 0
    for bi in b:
        if bi == "b":
            s += str(n) + bi
            n = 0
        else:
            n += 1
    s += str(n)
    return s.replace("0", "")


def decode(s):
    b = []
    for si in s:
        if si == "b":
            b += ["b"]
        else:
            b += ["."] * int(si)

    return b


def solve():
    s = input()
    if s == "#":
        return 1

    s = s.split("/")
    a, b, c, d = map(int, input().split())

    board = [decode(si) for si in s]
    board[a - 1][b - 1] = "."
    board[c - 1][d - 1] = "b"

    print("/".join([encode(b) for b in board]))


while not solve():
    ...
