#不正解

h, w = map(int, input().split())
S = [input() for i in range(h)]
x = [-1] * 2
y = [-1] * 2
xCnt = 0
yCnt = 0
i = 0
while i < h and xCnt < 2:
    s = S[i]
    if "o" in s:
        y[yCnt] = i
        yCnt += 1
        j = 0
        while j < w and s[j] != "o":
            j += 1
        x[xCnt] = j
        xCnt += 1
    i += 1

print(abs(x[1] - x[0]) + abs(y[1] - y[0]))