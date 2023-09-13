#正解

a, b = map(int, input().split())

ans = abs(b - a)
if ans == 1 or ans == 9:
    print("Yes")
else:
    print("No")