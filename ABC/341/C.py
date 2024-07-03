h, w, n = map(int, input().split())
t = list(input())
s = [list(input()) for _ in range(h)]


def move(i, j):
    for m in t:
        if m == "U":
            i -= 1
        elif m == "D":
            i += 1
        elif m == "L":
            j -= 1
        else:
            j += 1

        if s[i][j] == "#":
            return 0

    return 1


ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            ans += move(i, j)

print(ans)
