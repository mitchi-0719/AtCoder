#正解

n = int(input())
t = input()

point = [0, 0]
index = 0
xy = 1

for i in range(n):
    if t[i] == 'S':
        point[index] += xy
    else:
        if index == 0:
            xy *= -1
        index = (index + 1) % 2

print(point[0], point[1])