#正解

a, b, c, d = map(int, input().split())

d += 1
if d == 60:
    d = 0
    c += 1
    if c == 24:
        c == 0

taka = a * 60 + b
aoki = c * 60 + d

if taka < aoki:
    print("Takahashi")
else:
    print("Aoki")