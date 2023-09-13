n, m = map(int, input().split())

s = []
p = []

for i in range(n):
    s.append(input())

def judge(i, j):
    if not(set(s[i+3][j:j+4]) == set(s[i+5][j+5:j+9]) == {"."}):
        return False

    for k in range(i, i+4):
        if not(s[k][j+3] == s[k+5][j+5] == "."):
            return False

    for k in range(i, i+3):
        for l in range(j, j+3):
            if s[k][l] == "." or s[k+6][l+6] == ".":
                return False
    return True

for i in range(n-8):
    for j in range(m-8):
        if judge(i, j):
            p.append([i+1, j+1])

for i in p:
    print(*i)