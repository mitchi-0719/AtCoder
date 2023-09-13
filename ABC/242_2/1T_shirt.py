#正解

a, b, c, x = map(int, input().split())

if a >= x:
    print(1)
elif x <= b:
    ans = c / (b - a)
    print(ans)
else:
    print(0)