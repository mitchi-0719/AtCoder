#正解

import math

n, k = map(int, input().split())

A = list(map(int, input().split()))

X = [0] * n
Y = [0] * n

for i in range(n):
    X[i], Y[i] = map(int, input().split())

li = [[0 for i in range(k)] for j in range(n)]

def get_dist(x1, y1, x2, y2):
    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return d


for i in range(k):
    for j in range(n):
        li[j][i] = get_dist(X[A[i] - 1], Y[A[i] - 1], X[j], Y[j])

min_li = []

for i in range(n):
    min_li.append(min(li[i]))

print(math.sqrt(max(min_li)))