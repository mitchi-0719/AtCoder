# AC

n = int(input())
s = [input() for _ in range(n)]

direct = [[1, 0],
            [0, 1],
            [1, 1],
            [-1, 1]]

for i in range(n):
    for j in range(n):
        for k in range(4):
            cnt = 0
            for l in range(6):
                bi = direct[k][0] * l + i
                bj = direct[k][1] * l + j
                if bi < 0 or n <= bi or bj < 0 or n <= bj:
                    break
                if s[bi][bj] == "#":
                    cnt += 1
            else:
                if cnt >= 4:
                    print("Yes")
                    exit()

print("No")