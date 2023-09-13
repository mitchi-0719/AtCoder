n = int(input())
t = [0] * n
x = [0] * n
y = [0] * n

T, X, Y = 0, 0, 0
check = True

for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())

for i in range(n):
    if i == 0:
        T = t[i]
        X = x[i]
        Y = y[i]
    else:
        T = t[i] - t[i - 1]
        X = abs(x[i] - x[i - 1])
        Y = abs(y[i] - y[i - 1])

    dis = X + Y
    mods = T - dis
    if mods < 0 or mods % 2 == 1:
        print("No")
        check = False
        break


if check == True:
    print("Yes")