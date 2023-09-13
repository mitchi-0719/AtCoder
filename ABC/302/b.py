h, w = map(int, input().split())

s = [int(input()) for _ in range(h)]

st = "snuke"

for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            if j < w and s[i][j] == "n":
                
            if 