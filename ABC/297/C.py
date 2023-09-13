h, w = map(int, input().split())
s = []

for i in range(h):
    s.append(list(input()))
    for j in range(1, w):
        if s[i][j-1] == s[i][j] == "T":
            s[i][j-1] = "P"
            s[i][j] = "C"
    print(*s[i], sep="")