import numpy as np

n = int(input())
sx, sy, tx, ty = map(int, input().split())

x = []
y = []
r = []

touch_matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    X, Y, R = map(int, input().split())
    x.append(X)
    y.append(Y)
    r.append(R)

for i in range(n):
    for j in range(i+1, n):
        a = np.array([x[i], y[i]])
        b = np.array([x[j], y[j]])

        dist = np.linalg.norm(a-b)
        if dist <= r[i]+r[j] and abs(r[i]-r[j]) < dist:
            touch_matrix[i][j] = 1
            touch_matrix[j][i] = 1

        S = np.array([sx, sy])
        T = np.array([tx, ty])
        dist_s = np.linalg.norm(a-S)
        dist_t = np.linalg.norm(a-T)

        if dist_s == r[i]:
            s = i
        elif dist_t == r[i]:
            t = i

def sear(behind, start, goal):
    if set(touch_matrix[start]) != {0}:
        for i in range(n):
            if i != start and touch_matrix[start][i] == 1:
                sear(start, i, goal)
                touch_matrix[start][i] = 0
    elif 

if s == t:
    print("Yes")
else:
    sear(-1, s, t)