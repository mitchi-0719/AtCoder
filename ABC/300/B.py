def solve(s, t):
    for i in range(h):
        for j in range(w):
            if b[i][j] != a[(i + s) % h][(j + t) % w]:
                return False
    return True


h, w = map(int, input().split())

a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]

for s in range(h):
    for t in range(w):
        if solve(s, t):
            print("Yes")
            exit()

print("No")
