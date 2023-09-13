n = int(input())
x = []
y = []

for i in range(n):
    X, Y = map(int, input().split())

    x.append(X)
    y.append(Y)

print(x, y)