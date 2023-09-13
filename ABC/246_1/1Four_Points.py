xy = [input().split() for l in range(3)]

if xy[0][0] == xy[1][0]:
    point_x = xy[2][0]
elif xy[0][0] == xy[2][0]:
    point_x = xy[1][0]
else:
    point_x = xy[0][0]

if xy[0][1] == xy[1][1]:
    point_y = xy[2][1]
elif xy[0][1] == xy[2][1]:
    point_y = xy[1][1]
else:
    point_y = xy[0][1]

print(point_x, point_y)