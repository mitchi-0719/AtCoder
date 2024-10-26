board = [[True for _ in range(8)] for __ in range(8)]

for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == "#":
            for k in range(8):
                board[i][k] = False
            for k in range(8):
                board[k][j] = False

print(sum([b.count(True) for b in board]))
